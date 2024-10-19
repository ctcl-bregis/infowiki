// NetWiki - CTCL 2024
// File: /src/main.rs
// Purpose: Webserver
// Created: October 17, 2024
// Modified: October 19, 2024

use actix_web::{web, App, HttpServer};
use lysine::Lysine;
use netwiki::{loadconfig, Config};
use sqlx::Connection;

use log::{debug, info, warn, LevelFilter, SetLoggerError};
use log::{Record, Level, Metadata};

pub use netwiki::namespaces::*;
use setup::setuproute;

struct SimpleLogger;

impl log::Log for SimpleLogger {
    fn enabled(&self, metadata: &Metadata) -> bool {
        metadata.level() <= Level::max()
    }

    fn log(&self, record: &Record) {
        if self.enabled(record.metadata()) {
            println!("{} - {}", record.level(), record.args());
        }
    }

    fn flush(&self) {}
}

static LOGGER: SimpleLogger = SimpleLogger;

pub fn init(levelfilter: &str) -> Result<(), SetLoggerError> {
    let levelfilter = match levelfilter {
        "off" => LevelFilter::Off,
        "error" => LevelFilter::Error,
        "warn" => LevelFilter::Warn,
        "info" => LevelFilter::Info,
        "debug" => LevelFilter::Debug,
        "trace" => LevelFilter::Trace,
        _ => panic!("Invalid log level for debugloglevel in config.json")
    };

    log::set_logger(&LOGGER)
        .map(|()| log::set_max_level(levelfilter))
}

#[actix_web::main]
async fn main() -> Result<(), std::io::Error> {

    let configexists = match std::fs::exists("config.json") {
        Ok(b) => b,
        Err(e) => return Err(e)
    };

    if configexists {
        let cfg = loadconfig().unwrap();
        
        HttpServer::new(|| {
            App::new()
        })
        .bind((cfg.bindip, cfg.bindport))?.run().await
    } else {
        // Don't work on the setup utility until the app is actually done
        init("debug").unwrap();
        
        HttpServer::new(|| {
            let lysine = Lysine::new("templates/setup/**/*.lish").unwrap();

            App::new()
                .service(web::resource("/setup/{page:.*}").route(web::get().to(setuproute)))
                .app_data(web::Data::new(lysine))
        })
        .bind(("0.0.0.0", 8000))?.run().await
    }

    
}
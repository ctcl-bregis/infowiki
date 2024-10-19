// NetWiki - CTCL 2024
// File: /src/lib.rs
// Purpose: Globally defined types and functions
// Created: October 17, 2024
// Modified: October 19, 2024

use std::io::{Error, ErrorKind, Result};
use std::fs::{self, exists};
use std::path::Path;
use serde_json::value::Value;
use serde::{Serialize, Deserialize};

pub mod namespaces;

#[derive(Serialize, Deserialize)]
pub struct CacheMemcached {
    pub url: String,
    pub exp: u32,
}

#[derive(Serialize, Deserialize)]
pub struct CacheNone {}

#[derive(Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum CacheConfig {
    #[serde(alias = "memcached")]
    Memcached(CacheMemcached),
    #[serde(alias = "none")]
    None(CacheNone)
}

#[derive(Serialize, Deserialize)]
pub struct Config {
    pub bindip: String,
    pub bindport: u16,
    pub sitename: String,
    pub siteurl: String,
    pub cache: CacheConfig
}

pub fn readfile<P: AsRef<Path>>(path: P) -> Result<String> {
    match exists(&path) {
        Ok(b) => match b {
            true => (),
            // Why does this line have to mention "error" three times for a single string?
            false => return Err(Error::new(ErrorKind::NotFound, "File {path} does not exist"))
        }
        Err(e) => return Err(e)
    }

    let content = match fs::read_to_string(path) {
        Ok(c) => c,
        Err(e) => return Err(e)
    };
    
    Ok(content)
}

pub fn loadconfig() -> Result<Config>{
    let configjson = readfile("config.json")?;
    let config: Config = serde_json::from_str(&configjson)?;

    Ok(config)
}
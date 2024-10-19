// NetWiki - CTCL 2024
// File: /src/setup/mod.rs
// Purpose: Setup module definition
// Created: October 18, 2024
// Modified: October 19, 2024

use actix_web::{web, Error, HttpRequest, HttpResponse, Responder};

use crate::Config;


pub async fn setuproute(req: HttpRequest, page: web::Path<String>) -> Result<impl Responder, Error> {
       
    

    Ok(HttpResponse::Ok())
}
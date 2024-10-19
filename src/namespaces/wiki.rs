// NetWiki - CTCL 2024
// File: /src/namespaces/wiki.rs
// Purpose: Wiki namespace
// Created: October 19, 2024
// Modified: October 19, 2024

use actix_web::{web, Error, HttpRequest, HttpResponse, Responder};

use crate::Config;


pub async fn pageroute(req: HttpRequest, page: web::Path<String>) -> Result<impl Responder, Error> {
    
    

    Ok(HttpResponse::Ok())
}
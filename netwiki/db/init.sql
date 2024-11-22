DROP TABLE IF EXISTS pages;

CREATE TABLE pages (
    page_path TEXT COLLATE utf8_bin NOT NULL,
    page_title VARCHAR(255) COLLATE utf8_bin NOT NULL,
    page_content TEXT,
    page_modified TIMESTAMP,
    page_created TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO pages VALUES (
    "main_page/",
    "Main Page",
    "This is the default page of the wiki",
    NOW(),
    NOW()
);

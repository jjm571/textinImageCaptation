# textinImageCaptation
Scanning postcard images with text



Database Table Example
CREATE TABLE ocr_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    extracted_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


see: https://chatgpt.com/c/68a57d39-99d4-832b-8db9-2741518f087b

# News API

## Overview
The News API is a FastAPI-based project that provides a news summarization and recommendation service using Sentence-BERT and ChromaDB for vector storage. The API fetches news from supported websites (e.g., Indian Express) by scraping them and stores the data in a SQLite database. Summarized and similar news articles can be retrieved, and users need a token to access the API, which is created during the login process. The service maintains a cache of articles up to one month old.

## Features
- **News Summarization**: Summarizes the scraped news articles using Sentence-BERT.
- **Similar News Recommendations**: Provides similar news articles based on the content.
- **Token-Based Authentication**: Users must be authenticated to access the API, and a token is generated upon login.
- **SQLite Database Storage**: Stores all scraped news articles in a SQLite database for up to one month.
- **News Scraping**: Fetches news from supported websites, currently including:
  - Indian Express
  - (Add more sources as required)
- **Bug Awareness**: Known issues include occasional inaccurate summaries and other minor bugs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-api.git
   cd news-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python create_db.py
   ```

4. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### User Authentication

#### Login
- **URL**: `/auth/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "your_access_token",
    "token_type": "bearer"
  }
  ```

### News Summarization

#### Get Summarized News
- **URL**: `/news/summarize/{article_id}`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
    "article_id": "123",
    "title": "News Title",
    "summary": "Summarized content of the news article...",
    "source": "Indian Express",
    "published_at": "2023-09-25"
  }
  ```

### Similar News

#### Get Similar News
- **URL**: `/news/similar/{article_id}`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  [
    {
      "article_id": "456",
      "title": "Similar News Title",
      "summary": "Summary of the similar news article...",
      "source": "Indian Express",
      "published_at": "2023-09-20"
    }
  ]
  ```

### Fetch News (Scraping)
- **URL**: `/news/fetch`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Body**:
  ```json
  {
    "source": "indianexpress",
    "url": "https://indianexpress.com/some-news-article"
  }
  ```
- **Response**:
  ```json
  {
    "article_id": "789",
    "title": "Fetched News Title",
    "summary": "Automatically generated summary...",
    "source": "Indian Express",
    "published_at": "2023-09-26"
  }
  ```

## Bugs and Known Issues
- **Summarization**: The summarization model does not always produce perfect results and may miss key points in some cases.
- **Other Bugs**: There may be occasional bugs related to article fetching, authentication, or recommendation accuracy.

## Future Improvements
- **Model Optimization**: Improving the summarization algorithm to generate more accurate summaries.
- **Expand Supported Websites**: Adding more news sources to the scraping service.
- **Error Handling**: Enhanced handling of edge cases and better bug management.
  
## Tech Stack
- **Framework**: FastAPI
- **Database**: SQLite
- **Text Embedding**: Sentence-BERT
- **Vector Database**: ChromaDB
- **Web Scraping**: Custom Scraper
- **Authentication**: OAuth2 with JWT Tokens

## License
This project is licensed under the MIT License.

---

This README gives a clear picture of your News API project with setup instructions, a list of features, API endpoint documentation, and known issues. You can customize it further to match your specific needs!
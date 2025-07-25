## File Upload and Management UI

Built using React, Bootstrap, and Axios to consume REST APIs exposed by a FastAPI backend. Features include listing, previewing, and downloading uploaded files.

## Use of React

- React for component-based UI rendering
- React Router DOM for navigation (Home, Preview pages)
- Axios for API communication
- Bootstrap for styling

## How to Run (Frontend)

```bash
cd frontend
npm install
npm start
```

Runs on: `http://localhost:3000`

## File Upload Backend API

Implements REST APIs to handle file upload, metadata storage, and file download. Uses local storage and SQLite database.

## Use of FastAPI

- FastAPI for API development and request handling
- SQLModel for ORM and database operations (SQLite)
- Python-multipart for handling file uploads
- Uvicorn as the ASGI server

## How to Run (Backend)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Runs on: `http://localhost:8000`

## Frontend Architecture 
![Frontend](./frontend/public/Frontend.png)

## Backend Architecture 
![Backend](./frontend/public/Backend.png)

## Full Stack Architecture 
![Backend](./frontend/public/Fullstack.png)

## Frontend Page Design
![Frontend Page Design](./frontend/public/FrontendDesign.png)

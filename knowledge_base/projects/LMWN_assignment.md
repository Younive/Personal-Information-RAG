# Project Deep Dive: Restaurant Recommendation API

This project is a high-performance HTTP API server for a restaurant recommendation system, built as a comprehensive solution to the take-home test assignment for the LINE MAN Wongnai Junior Machine Learning Engineer position candidate in January 2024. 

* **Project Link:** [GitHub Repository](https://github.com/Younive/LMWN-Assignment-MLOps-Hand-Ons.)

---

### Problem Statement & Goal
The primary goal was to build a stable, scalable, and production-ready service capable of delivering restaurant recommendations based on a pre-trained `NearestNeighbors` model.  The system was required to meet strict performance targets: serving 30 requests per second with a 90th percentile response time under 100 milliseconds. 

### My Role
I was the sole developer for this end-to-end project, responsible for system architecture design, database optimization, API development, caching strategy, performance testing, and final deployment.

### Architecture & Methodology
The final implementation is a robust, production-ready system featuring several key optimizations to ensure stability and performance under concurrent load. 

* **Web Server & Framework**: The application is served by a multi-process **Gunicorn** server managing synchronous **Uvicorn** workers, which provides true parallelism and stability under high load.  The API itself is built with **FastAPI** for its high performance and automatic data validation capabilities. 
* **Database**: **PostgreSQL** is used to store user feature data and restaurant location data.  To ensure millisecond-level query times, critical database indexes were added to `users(user_id)` and `restaurants(h3_index)`. 
* **Centralized Caching & Pre-warming**: A high-performance, in-memory **Redis** cache is shared by all Gunicorn worker processes to significantly boost performance.  The cache is pre-warmed using a **Gunicorn `on_starting` server hook** that runs a one-time, memory-efficient batch process to load all user data, ensuring the cache is "hot" when workers start. 
* **Recommendation Logic**: The core logic uses a pre-trained Scikit-Learn `NearestNeighbors` model to find recommendations.  To optimize this process, an **H3-based geospatial pre-filtering** strategy was implemented to dramatically reduce the search space for nearby restaurants. 
* **Data & Model Versioning**: The large `user.parquet` data file is tracked using **DVC (Data Version Control)** to keep the Git repository lightweight.  The pre-trained model is stored as `model.pkl`. 

### Key Technical Challenges & Solutions
The journey from a functional prototype to a stable, optimized system involved solving several critical engineering challenges:

1.  **Challenge: Application Instability & Deadlocks**
    * **Problem**: An initial `async` architecture that used `run_in_threadpool` for blocking calls suffered from severe freezes and connection timeouts under concurrent load due to complex deadlocks. 
    * **Solution**: The architecture was pivoted to a simpler, more robust multi-process model using Gunicorn with synchronous Uvicorn workers.  This eliminated the shared resource contention and provided true parallelism, an industry-standard approach for deploying Python web apps. 

2.  **Challenge: Severe Database Performance Bottleneck**
    * **Problem**: Initial diagnostic tests revealed that a single, un-indexed query to the user database was taking approximately 544 ms, making it impossible to meet the latency requirements. 
    * **Solution**: The single greatest performance gain came from adding an index to the `users.user_id` column, which reduced the query's latency by over 90%. 
    * **Additional Refinement**: To make queries safer and more maintainable, raw SQL f-strings were replaced with **SQLAlchemy's `Table` construct**. 

3.  **Challenge: "Out of Memory" (OOM) Errors Under Load**
    * **Problem**: Load tests caused API workers to crash with OOM errors due to the high memory footprint of creating pandas DataFrames on every request. 
    * **Solution**: The code was optimized to convert data from the database directly into a lightweight **NumPy array**.  NumPy's memory efficiency solved the OOM crashes and stabilized the server under high concurrency. 

### Technologies & Tools Used
* **API & Server:** FastAPI, Gunicorn, Uvicorn 
* **Database & Cache:** PostgreSQL, Redis 
* **Data Science & ML:** Scikit-Learn, NumPy, pandas (for initial data loading) 
* **Database Interaction:** SQLAlchemy 
* **Deployment & Infrastructure:** Docker, Docker Compose 
* **Data Versioning:** DVC (Data Version Control) 
* **Performance Testing:** Locust 

### Personal Learnings
This project was a comprehensive, end-to-end exercise in deploying a machine learning model as a high-performance, production-ready service. The journey revealed several critical engineering lessons: 

* **Architecture is Foundational:** I learned that choosing the right concurrency model (multi-process Gunicorn over a complex async setup) is fundamental to application stability. 
* **Optimize the Database First:** My biggest takeaway was that database optimization is the mandatory first step before any code-level changes. Adding a single index had a more significant impact than any other optimization. 
* **Memory Management is Crucial:** I gained practical experience in memory optimization, learning that library choices (NumPy vs. pandas) within a request cycle have a massive impact on an application's stability under load. 
* **Inference as a System Component:** The final performance bottleneck was the CPU time of the `model.kneighbors()` inference itself. This emphasized that an ML Engineer must consider the inference performance of a model as a critical part of the system design, not just its predictive accuracy. 
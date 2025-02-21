Overview:

NewsApp is a modern Android application that provides users with the latest news from various sources. Built with MVVM architecture, the app ensures a clean separation of concerns and better maintainability. It integrates Room for offline storage, Navigation Component for seamless screen transitions, Coroutines for asynchronous operations, and Retrofit for efficient API communication.

Key Features:

> Latest News Fetching – Retrieves real-time news articles from a REST API using Retrofit.
> Offline Support – Saves articles using Room Database for offline reading.
> MVVM Architecture – Ensures modularity, testability, and a clear separation of concerns.
> Seamless Navigation – Uses Navigation Component for smooth transitions between screens.
> Efficient Performance – Leverages Kotlin Coroutines for background operations and improved responsiveness.

Technical Implementation

🔹 MVVM Architecture:
ViewModel: Manages UI-related data and handles business logic.
Repository: Acts as a single source of truth, fetching data from the API and local database.
LiveData: Ensures real-time UI updates.
🔹 Retrofit for API Calls:
Fetches news articles from a REST API using Retrofit.
Parses JSON responses into Kotlin data classes.
🔹 Room Database for Offline Storage:
Saves news articles locally for offline access.
Uses DAO (Data Access Object) for database interactions.
🔹 Navigation Component:
Handles in-app navigation between screens like Home, Favorites, and Article Details.
🔹 Coroutines for Background Processing:


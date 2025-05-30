# Django Online Store

A simple online store application built with Django and Bootstrap.

## Project Status

**This project is currently under development.** New features and improvements are being actively added. The shopping cart functionality has been recently implemented, and further enhancements are planned.

## Features (Implemented and Planned)

* **User Authentication:**
    * User signup
    * User login
    * User logout
* **Shop:**
    * Homepage displaying all products
    * Individual product detail pages
    * Product categories (structure in place)
    * Display of sale prices
* **Shopping Cart:**
    * Add products to cart (for both authenticated and guest users)
    * View cart items
    * Update item quantities in the cart
    * Remove items from the cart
    * Display total cart price and item count
* **Planned Features:**
    * Checkout process
    * Order history for users
    * Product search and filtering
    * Admin panel improvements for product and order management
    * User profile page
    * Product reviews and ratings

## Technologies Used

* **Backend:**
    * Python
    * Django
* **Frontend:**
    * HTML
    * CSS (Bootstrap 5)
    * JavaScript (minimal, via Bootstrap components)
* **Database:**
    * SQLite (for development)

## Project Structure

The project is organized into the following Django apps:

* `shop`: Handles product listings, product details, user authentication, and general store pages (home, about).
* `cart`: Manages the shopping cart functionality.
* `main`: The main project directory containing settings and root URL configurations.

## Setup and Installation (General Steps)

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd <project-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt 
    ```
    Key dependencies include:
    * `Django`
    * `python-dotenv` 

4.  **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will typically be available at `http://127.0.0.1:8000/`.

## Contributing

As this project is under active development, contributions and suggestions are welcome. Please feel free to open an issue or submit a pull request.

---

*This README provides a general overview. Specific details may be updated as the project progresses.*


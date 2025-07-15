# MyShop - Django E-Commerce Platform

## Overview

MyShop is a full-featured E-Commerce web application for online clothing shopping, built with Django. It allows users to browse products, add items to a cart, apply coupons, place orders, and pay securely. The project demonstrates advanced Django concepts, asynchronous task processing with Celery, PDF generation, and integration with payment gateways.

## Features
- Product catalog with categories
- Shopping cart with session management
- Order placement and checkout
- Coupon/discount system
- Payment gateway integration (Zibal)
- PDF invoice generation
- Asynchronous task processing (Celery, RabbitMQ)
- Redis caching
- Admin dashboard
- Responsive UI (Bootstrap)

## Technology Stack
- **Backend:** Django 4.2
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** SQLite (default, can be changed)
- **Task Queue:** Celery, RabbitMQ
- **Cache/Session:** Redis
- **PDF Generation:** WeasyPrint
- **Containerization:** Docker, Docker Compose

## Project Structure
```
MyShop/
  ├── cart/         # Cart management
  ├── contact/      # Contact form
  ├── coupon/       # Coupon/discount system
  ├── order/        # Order and checkout
  ├── shop/         # Product catalog
  ├── zibal/        # Payment gateway integration
  ├── Shop-core/    # Project settings and core config
  ├── static/       # Static files (CSS, JS, images)
  ├── templates/    # Base and shared templates
  ├── media/        # Uploaded product images
  ├── requirements.txt
  ├── docker-compose.yml
  └── Dockerfile
```

## Getting Started

### Prerequisites
- Docker & Docker Compose (recommended)
- Python 3.10+ (if running locally)

### Quick Start with Docker
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd MyShop
   ```
2. **Build and start the services:**
   ```bash
   docker-compose up --build
   ```
3. **Access the app:**
   - Web: [http://localhost:8000](http://localhost:8000)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Manual Setup (Local Development)
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set environment variables:**
   - Create a `.env` file in the root directory (see `Shop-core/settings.py` for required variables like `DJANGO_SECRET_KEY`, `REDIS_HOST`).
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Run development server:**
   ```bash
   python manage.py runserver
   ```
5. **Start Celery worker (in a new terminal):**
   ```bash
   celery --app=Shop-core worker -l INFO
   ```

## Main Endpoints
- `/` - Home page
- `/shop/` - Product listing
- `/cart/` - Shopping cart
- `/order/` - Checkout and orders
- `/zibal/` - Payment processing
- `/coupon/` - Apply coupons
- `/contact/` - Contact form
- `/admin/` - Admin dashboard

## Core Apps & Models
- **shop:** `Product`, `Category`
- **cart:** Session-based cart logic
- **order:** `Order`, `OrderItem`
- **coupon:** Coupon codes and discounts
- **zibal:** Payment gateway integration

## Learning Highlights
- Building a shopping cart from scratch
- Session management in Django
- Asynchronous tasks with Celery & RabbitMQ
- PDF generation with WeasyPrint
- Payment gateway integration

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is for educational purposes. 

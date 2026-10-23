# Wobega Backend 🛍️

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC2927?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**Wobega** is a production-grade, highly scalable multi-vendor e-commerce backend system built using modern Python frameworks and relational database design. It implements a robust service-oriented architecture capable of handling multi-tenant vendor marketplaces, centralized master product catalogs, granular inventory control, secure authentication, and dynamic order lifecycle tracking.

---

## 🚀 Key Architectural Highlights

- **Multi-Vendor Marketplace Engine**: Decouples the global master product catalog (`products`) from individual merchant store listings (`businesses` and `product_listings`), allowing multiple vendors to offer competing prices and stocks for the same core item.
- **Service-Oriented Layered Architecture**: Strictly separates concerns between HTTP routing (`routers/`), database business logic (`services/`), ORM data models (`models.py`), and data validation contracts (`schemas.py`).
- **Robust Inventory & Order Management**: Includes transactional stock deductions during checkout and automatic stock restocking safeguards when customer orders are cancelled or modified.
- **Enterprise Security**: Implements industry-standard cryptographic password hashing (`bcrypt`/`passlib`) and protected database sessions via dependency injection (`Depends(get_db)`).

---

## 🛠️ Tech Stack

- **Framework**: FastAPI (Asynchronous high-performance web framework)
- **Database & ORM**: PostgreSQL managed via SQLAlchemy Core/ORM & pgAdmin 4
- **Validation & Serialization**: Pydantic v2
- **Security**: Passlib & Bcrypt for secure credential management
- **Server**: Uvicorn (ASGI server with live reload capabilities)

---

## 🗄️ Database Entity-Relationship Overview

The relational schema is meticulously mapped across **8 normalized tables**:
1. **`users`**: Central user identity management with role-based segregation (`admin`, `customer`, `seller`).
2. **`businesses`**: Storefront profiles linked directly to marketplace owner accounts.
3. **`products`**: Centralized global catalog for master items (Categories, Brands, Descriptions).
4. **`product_listings`**: Vendor-specific offers linking merchants to master products with custom pricing and stock.
5. **`carts` & `cart_items`**: Transient shopping session storage tracking active cart entries per user.
6. **`orders` & `order_items`**: Immutable checkout history snapshots tracking fulfillment statuses (*Order Confirmed, Shipped, Out for Delivery, Cancelled*).

---

## 📂 Project Structure

```text
backend/
│
├── app/
│   ├── routers/
│   │   ├── api.py
│   │   ├── carts.py
│   │   ├── orders.py
│   │   ├── products.py
│   │   ├── sellers.py
│   │   └── users.py
│   │
│   ├── services/
│   │   ├── admin_service.py
│   │   ├── cart_service.py
│   │   ├── order_services.py
│   │   ├── product_listing_service.py
│   │   ├── product_service.py
│   │   ├── seller_service.py
│   │   └── user_service.py
│   │
│   ├── database.py       # SQLAlchemy engine & session maker configuration
│   ├── main.py           # FastAPI application entry point & router aggregation
│   ├── models.py         # SQLAlchemy ORM table definitions
│   ├── schemas.py        # Pydantic data validation & serialization contracts
│   └── security.py       # Password hashing & verification utilities
│
├── .env                  # Environment variables (Database URL credentials)
├── requirements.txt      # Project dependency list
└── README.md
```

---

## ⚙️ Getting Started & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/wobega-backend.git
cd wobega/backend
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root of the `backend` directory and add your PostgreSQL connection string:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wobega_db
```

### 5. Run the Server
Launch the application with live-reloading enabled via Uvicorn:
```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation & Testing

Once the server is running, you can explore and test all endpoints interactively via FastAPI's built-in documentation interfaces:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 💡 Future Enhancements
- [ ] Implement JWT (JSON Web Token) Bearer authentication for route protection.
- [ ] Integrate Stripe/Razorpay payment gateway webhooks for checkout processing.
- [ ] Add Redis caching layer for high-frequency product catalog searches.

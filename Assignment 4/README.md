# Shopping Cart Management System

This Python program simulates an **online shopping cart management system**. It allows for managing an inventory of products, maintaining a product catalog, and enabling customers to add/remove items from their shopping cart. Purchases made by customers are reflected in the inventory to ensure accurate tracking of stock.

## Features

### 1. **Product Management**
- **Product Class**:
  - Represents individual products with attributes: `name`, `price`, and `category`.
  - Includes functionality for comparison and easy representation of products.
  
- **ProductCatalog Class**:
  - Maintains a list of all products available for purchase.
  - Provides functionalities to:
    - Add products to the catalog.
    - Categorize products into low, medium, and high price ranges.
    - Display all products in the catalog.

### 2. **Inventory Management**
- **Inventory Class**:
  - Manages the stock of products.
  - Supports adding and removing products and their quantities.
  - Provides access to product details such as price and quantity.
  - Displays the complete inventory in a user-friendly format.

### 3. **Shopping Cart**
- **ShoppingCart Class**:
  - Allows customers to:
    - Add items to their cart (ensures sufficient stock in inventory).
    - Remove items from their cart (returns stock to inventory).
    - View the contents of their cart and the total cost of items.
  - Tracks cart details per customer.

### 4. **File Integration**
- Load product and inventory data from external files.
- Supports CSV files with the following format: `product_name,price,quantity,category`.
- Functions:
  - `populate_inventory(filename)`: Reads inventory data from a file and populates the inventory.
  - `populate_catalog(filename)`: Reads product catalog data from a file and populates the product catalog.

## How It Works
1. **Classes**:
   - The system uses object-oriented programming to define classes for `Product`, `Inventory`, `ShoppingCart`, and `ProductCatalog`.
2. **File Input**:
   - Inventory and product catalog data are loaded from external files at runtime.
3. **Real-Time Inventory Updates**:
   - Adding/removing items from the shopping cart dynamically updates the inventory.

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    phone_number VARCHAR(20),
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE savings (
    savings_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    account_balance DECIMAL(10, 2) DEFAULT 0.00,
    account_type VARCHAR(50),
    interest_rate DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE equb_groups (
    equb_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    group_size INT,
    cycle_period INT, -- number of days for each cycle
    amount_per_cycle DECIMAL(10, 2) NOT NULL,
    start_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE equb_memberships (
    membership_id SERIAL PRIMARY KEY,
    equb_id INT REFERENCES equb_groups(equb_id),
    user_id INT REFERENCES users(user_id),
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(20) DEFAULT 'member' -- could be 'admin' or 'member'
);

CREATE TABLE blogs (
    blog_id SERIAL PRIMARY KEY,
    author_id INT REFERENCES users(user_id),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    transaction_type VARCHAR(20), -- deposit, withdrawal, loan repayment, etc.
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

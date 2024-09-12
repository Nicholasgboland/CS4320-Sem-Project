-- SQL file to initialize DB
CREATE TABLE property (
  property_id SERIAL NOT NULL,
  name VARCHAR(100) NOT NULL,
  street_addr VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  county VARCHAR(100),
  state_abrv VARCHAR(2) NOT NULL,
  zip NUMBER(5) NOT NULL,
  purchase_date DATE,
  sqr_ft NUMERIC(10,5),
  price_per_sqqr_ft NUMERIC(50,2),
  purchase_price NUMERIC(50,2),
  market_price NUMERIC(50,2),
  num_of_units NUMERIC(3),
  notes VARCHAR(200),
  PRIMARY KEY(property_id),
  UNIQUE(street_addr, city, state_abrv, zip)
);

CREATE TABLE unit (
  unit_id SERIAL NOT NULL,
  name VARCHAR(100) NOT NULL,
  unit_number VARCHAR(50) NOT NULL,
  sqr_ft NUMERIC(10,5),
  price_per_sqqr_ft NUMERIC(50,2),
  notes VARCHAR(200),
  PRIMARY KEY(unit_id),
  CONSTRAINT unit_property_fk FOREIGN KEY(unit_id) REFERENCES property(property_id)
);

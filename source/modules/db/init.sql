-- SQL file to initialize DB
CREATE TABLE property (
  property_id SERIAL NOT NULL, -- Unique internal identifier for each property
  name VARCHAR(100) NOT NULL, -- Name of the property
  street_addr VARCHAR(100) NOT NULL, -- Property's street address
  city VARCHAR(100) NOT NULL, -- Property's city
  county VARCHAR(100), -- Porperty's
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
  property_id INTEGER NOT NULL,
  name VARCHAR(100) NOT NULL,
  unit_number VARCHAR(50) NOT NULL,
  sqr_ft NUMERIC(10,5),
  price_per_sqqr_ft NUMERIC(50,2),
  notes VARCHAR(200),
  PRIMARY KEY(unit_id),
  CONSTRAINT unit_prop_fk FOREIGN KEY(property_id) REFERENCES property(property_id)
);

CREATE TABLE tenant (
  tenant_id SERIAL NOT NULL,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  notes VARCHAR(200)
);

CREATE TABLE rental_agreement (
  agreement_id SERIAL NOT NULL,
  property_id INTEGER NOT NULL,
  tenant_id INTEGER NOT NULL,
  contract_num VARCHAR(50),
  contract_docs TEXT [],
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  curr_rent NUMERIC(50,2) NOT NULL,
  accepted BOOLEAN NOT NULL,
  active BOOLEAN NOT NULL,
  payment_sched VARCHAR(50),
  notes VARCHAR(200),
  next_increase DATE,
  last_increase DATE,
  PRIMARY KEY(agreement_id),
  CONSTRAINT agr_prop_fk FOREIGN KEY(property_id) REFERENCES property(property_id),
  CONSTRAINT agr_ten_fk FOREIGN KEY(tenant_id) REFERENCES tenant(tenant_id)
);

CREATE TABLE rental_invoice (
  invoice_id SERIAL NOT NULL,
  issue_date DATE NOT NULL,
  cash_date DATE,
  check_num VARCHAR(50),
  agreement_id INTEGER NOT NULL,
  tenant_id INTEGER NOT NULL,
  amount_paid NUMERIC(50,2) NOT NULL,
  notes VARCHAR(200),
  PRIMARY KEY(invoice_id),
  CONSTRAINT inv_ten_fk FOREIGN KEY(tenant_id) REFERENCES tenant(tenant_id),
  CONSTRAINT inv_agr_fk FOREIGN KEY(agreement_id) REFERENCES rental_agreement(agreement_id)
);

CREATE TABLE maint_report (
  maint_record_id SERIAL NOT NULL,
  maint_report_date DATE NOT NULL,
  property_id INTEGER NOT NULL,
  unit_id INTEGER,
  notes VARCHAR(200),
  PRIMARY KEY(maint_record_id),
  CONSTRAINT mr_prop_fk FOREIGN KEY(property_id) REFERENCES property(property_id),
  CONSTRAINT mr_unit_fk FOREIGN KEY(unit_id) REFERENCES unit(unit_id)
);

CREATE TABLE maint_report_item (
  maint_item_id SERIAL NOT NULL,
  maint_report_id INTEGER NOT NULL,
  maint_item_name VARCHAR(100) NOT NULL,
  notes VARCHAR(200),
  PRIMARY KEY(maint_item_id),
  CONSTRAINT mri_mr_fk FOREIGN KEY(maint_report_id) REFERENCES maint_report(maint_report_id)
);

CREATE TABLE maint_quote (
  maint_quote_id SERIAL NOT NULL,
  maint_report_id INTEGER NOT NULL,
  maint_quote_date DATE NOT NULL,
  quote_total NUMERIC(50,2) NOT NULL,
  PRIMARY KEY(maint_quote_id),
  CONSTRAINT mq_mr_fk FOREIGN KEY(maint_report_id) REFERENCES maint_report(maint_report_id)
);

CREATE TABLE maint_quote_item (
  quote_item_id SERIAL NOT NULL,
  maint_quote_id INTEGER NOT NULL,
  quote_item_name VARCHAR(100) NOT NULL,
  quote_item_cost NUMERIC(50,2),
  PRIMARY KEY(quote_item_id),
  CONSTRAINT mqi_mq_fk FOREIGN KEY(maint_quote_id) REFERENCES maint_quote(maint_quote_id)
);

CREATE TABLE maint_quote_invoice (
  maint_invoice_id SERIAL NOT NULL,
  maint_quote_id INTEGER NOT NULL,
  issue_date DATE NOT NULL,
  check_num VARCHAR(50),
  amount_paid NUMERIC(50,2) NOT NULL,
  notes VARCHAR(200),
  PRIMARY KEY(maint_invoice_id),
  CONSTRAINT mqv_mq_fk FOREIGN KEY(maint_quote_id) REFERENCES maint_quote(maint_quote_id)
);

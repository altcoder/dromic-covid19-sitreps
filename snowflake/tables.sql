CREATE TABLE IF NOT EXISTS ACA.COVID.DROMIC_COVID19_SITREPS_FAS(
  timestamp_pst TIMESTAMP_NTZ(9),
  sitrep NUMBER,
  office VARCHAR,
  latitude FLOAT,
  longitude FLOAT,
  standby_funds DECIMAL(24,2),
  ffp_quantity DECIMAL(24,2),
  ffp_total_cost DECIMAL(24,2),
  ofi_total_cost DECIMAL(24,2),
  nfi_total_cost DECIMAL(24,2),
  total DECIMAL(24,2)
);

CREATE TABLE IF NOT EXISTS ACA.COVID.DROMIC_COVID19_SITREPS_COA(
  timestamp_pst TIMESTAMP_NTZ(9),
  sitrep NUMBER,
  geolevel VARCHAR(16),
  is_plgu BOOLEAN,
  dswd_name VARCHAR,
  psgc_code NUMBER(9,0),
  psgc_name VARCHAR,
  dswd_province VARCHAR,
  psgc_province VARCHAR,
  psgc_provice_code NUMBER(9,0),
  dswd_region VARCHAR,
  psgc_region VARCHAR,
  psgc_region_code NUMBER(9,0),
  latitude FLOAT,
  longitude FLOAT,
  coa_dswd DECIMAL(24,2),
  coa_lgu DECIMAL(24,2),
  coa_ngo DECIMAL(24,2),
  coa_others DECIMAL(24,2),
  coa_total DECIMAL(24,2)
);

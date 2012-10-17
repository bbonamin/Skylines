ALTER TABLE igc_files ADD COLUMN timestamps timestamp without time zone[];
ALTER TABLE igc_files ADD COLUMN locations geometry(MultiPoint,4326);

CREATE INDEX idx_igc_files_locations
  ON igc_files
  USING gist
  (locations );

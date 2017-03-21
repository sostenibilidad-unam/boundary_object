import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import time

parser = argparse.ArgumentParser(description='set time step')
parser.add_argument('--prefijo', default='agebs_calles_geo_', help='prefijo de la capa')
args = parser.parse_args()

engine  = create_engine("postgresql+psycopg2://postgres:x@localhost/new")
conn = engine.connect()

s = text('CREATE TABLE "infra_c" (LIKE "agebs_c" INCLUDING ALL);')
conn.execute(s)

s = text('INSERT INTO public."infra_c"(id, geom, ageb_id) SELECT id, geom, ageb_id FROM public."agebs_c";')
conn.execute(s)

for i in range(1,20):
    
    s= text('ALTER TABLE "infra_c" ADD COLUMN t'+str(i)+' double precision;')
    conn.execute(s)
    
    s = text("UPDATE infra_c SET t"+str(i)+" = infra_h.infra FROM infra_h WHERE infra_h.ageb_id = infra_c.ageb_id AND timestep = "+str(i*12))
    conn.execute(s)

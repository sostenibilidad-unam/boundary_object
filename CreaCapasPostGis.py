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

for i in range(1,16):

    s = text('CREATE TABLE "agebs_p_geo_'+str(i)+'" (LIKE "agebs_p_geo" INCLUDING ALL);')
    conn.execute(s)
    
    s = text('INSERT INTO public."agebs_p_geo_'+str(i)+'"(id, geom, cvegeo, ageb_id, infra) SELECT id, geom, cvegeo, ageb_id, infra FROM public."agebs_p_geo";')
    conn.execute(s)
    
    s = text("UPDATE agebs_p_geo_"+str(i)+" SET infra = infra_h.infra FROM infra_h WHERE infra_h.ageb_id = agebs_p_geo_"+str(i)+".ageb_id AND timestep = "+str(i*10))
    conn.execute(s)

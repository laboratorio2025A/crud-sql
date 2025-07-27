import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://usr_polimusic_gr1:Politecnica1@sqlserver/BDD_PoliMusic_GR1?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
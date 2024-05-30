CREATE TABLE IF NOT EXISTS Partidas (
                    CODIGO_PARTIDA SERIAL PRIMARY KEY,
                    jugador1 TEXT,
                    jugador2 TEXT,
                    tablero_jugador1 JSONB,
                    tablero_jugador2 JSONB
                )
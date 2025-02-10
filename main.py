from server import SERVER
import uvicorn
import set

if __name__ == "__main__":
    sv = SERVER()
    uvicorn.run(sv.app, port= set.server_run_port)
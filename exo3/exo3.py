from flask import Flask, render_template
import platform, socket, os
from cpuinfo import get_cpu_info

# Get infos of the current computer
hostname = socket.gethostname()
cpu_infos = get_cpu_info()
machine = platform.machine()
os = os.name

# Computer Class
class Computer:
    def __init__(self, hostname, cpu_infos, machine, os):
         self._hostname = hostname
         self._cpu_infos = cpu_infos
         self._machine = machine
         self._os = os
      
    # Getter methods
    def get_hostname(self):
        return self._hostname
    def get_cpu_infos(self):
        return self._cpu_infos
    def get_machine(self):
        return self._machine
    def get_os(self):
        return self._os
      
    # Setter methods
    def set_hostname(self, x):
        self._hostname = x
    def set_cpu_infos(self, x):
        self._cpu_infos = x
    def set_machine(self, x):
        self._machine = x
    def set_os(self, x):
        self._os = x

currentComputer = Computer(hostname, cpu_infos['brand_raw'], machine, os)

app = Flask(__name__)

@app.route('/')
def exo3():
    return render_template('index.html',
     os=currentComputer.get_os(),
     hostname=currentComputer.get_hostname(),
     machine=currentComputer.get_machine(),
     cpu_infos=currentComputer.get_cpu_infos()
    )

if __name__ == "__main__":
    app.run(debug=True)

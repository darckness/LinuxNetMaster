import subprocess

# Abre um terminal e executa um comando
subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'comando_aqui; exec bash'])

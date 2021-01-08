from cx_Freeze import setup,Executable

setup(
	name="Exercice2",
	version="0.1",
	description = "Mise en formedesonnées sous format json",
	executables = [Executable("exercice2.py")]
	)
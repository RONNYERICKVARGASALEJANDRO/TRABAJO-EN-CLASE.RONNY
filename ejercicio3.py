class datos:
    variable=0

    def __init__(self,dato1="jejej"):
        self.informacion=dato1 

    def dato2(self):
      edad,peso=20,50
      nombre="ronny vargas"
      sexo="masculino"
      civil=True
      print(nombre,edad,peso)
#tuplas inmutables
      dt=('nice','666','ronny@gmail.com')

#listas mutables
      tipos=['programcion web', 'php', 'poo']
      tipos[1]='java'
      tipos.append('python')
#diccionario 
      docente={}
      docente={'nombre':'ronny','edad':50,'facultad':'ing'}
      docente['carrera']='bio'
      
      print(tipos,dt,docente)
      print(dt,dt[0],dt[0:1],dt[-1])
      print(tipos,tipos[2:],tipos[:1],tipos[::])
      print(docente,docente['ronny see'])
    


info= datos()
info.dato2()
print(info.informacion)


        
        
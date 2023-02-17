from core.asistencias.models import Facultad

# query = Universidad.objects.all()
# print(query)

#insertar
# u = Universidad()
# u.nombre = 'Universidad Nacional de Loja'
# u.direccion = 'Loja, La Argelia'
# u.save()

#edicion
# u = Universidad.objects.get(id=1)
# u.nombre = 'Universidad Nacional de Loja'
# u.save()
# print(u)

#eliminar
# try:
#     u = Universidad.objects.get(id=1)
#     u.delete()
#     u.save()
#     print(u)
# except Exception as e:
#     print(e)

# u = Universidad.objects.filter(nombre__icontains='unive').query
# print(u);

# for item in Universidad.objects.all()[:2]:
    # print(item.nombre)
# u = Universidad.objects.filter(nombre__startswith='Uni')[0]
# print(u.id)
#
# fac = Facultad()
# fac.nombre='Energia Y Recursos Naturales No Renovables'
# fac.universidad_id = u.id
# fac.save()

listFacultades = Facultad.objects.filter(universidad_id=1)
print(listFacultades[0].universidad.nombre)
from package_architecture.package_1.file_1 import a, b
print(a,b)

from package_architecture.package_1 import file_1
print(file_1.a, file_1.b)

from package_architecture.package_1 import file_1 as f
print(f.a, f.b)
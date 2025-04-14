# Imagen base de Node
FROM node:18

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos del proyecto (package.json y lock primero para optimizar cache)
COPY package*.json ./

# Instalamos dependencias
RUN npm install

# Copiamos el resto del código
COPY . .

# Puerto expuesto
EXPOSE 3000

# Comando para iniciar la app
CMD ["npm", "start"]

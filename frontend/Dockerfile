#use nginx runtime as base image
FROM nginx:alpine

#copy frontend build files to nginx runtime
COPY . /usr/share/nginx/html

#expose port 80
EXPOSE 80

#start nginx server
CMD ["nginx", "-g", "daemon off;"]
FROM rockylinux:9

RUN dnf -y install httpd wget zip unzip && dnf clean all

ADD https://www.tooplate.com/zip-templates/2121_wave_cafe.zip /var/www/html/

WORKDIR /var/www/html
RUN unzip -o 2121_wave_cafe.zip && \
    cp -r 2121_wave_cafe/* . && \
    rm -rf 2121_wave_cafe 2121_wave_cafe.zip

EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]


docker run --rm -it -v /tmp/demo/logs:/home/app/logs/ \
            -v /tmp/demo/logstash.yml:/usr/share/logstash/config/logstash.yml \
            -v /tmp/demo/logstash.conf:/usr/share/logstash/pipeline/logstash.conf  \
            -e xpack.security.enabled=false \
            -p 5228:5228/udp -p 5228:5228 docker.elastic.co/logstash/logstash:5.6.2 #bash #-f /usr/share/logstash/pipeline/logstash.conf

# Testing (g)nsq with blockade

Install [blockade][1] and then:

    docker build -t producer ./producer
    docker build -t consumer ./consumer
    sudo blockade up
    sudo blockade flaky consumer

[1]: https://github.com/dcm-oss/blockade


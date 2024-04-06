# PiHole

A compehensive guide to setting up your personal PiHole.

## OS Selection

- [DietPi]()
  - Lower Device Power Consumpion
  - Lean OS

## Hardening

- [Harden my pi running pihole?](https://discourse.pi-hole.net/t/harden-my-pi-running-pihole-install-ufw/5642/17)
- [Building a PiHole for Privacy and Performance](https://thesmashy.medium.com/building-a-pihole-for-privacy-and-performance-f762dbcb66e5)
- [Securing PiHole](https://discourse.pi-hole.net/t/securing-pihole/1155)

## Dual Setup

A second PiHole will be for redundancy, not for DNS balancing. Depending on your network and with two Pi-Holes running in parallel, the split between the two Pi-Holes is not predictable or controllable, although the first Pi-Hole listed as DNS usually receives the majority of the traffic. You won't have any control over the load balance if both Pi-Holes serve your entire network. But, you will have instant redundancy if one of the two Pi-Holes goes offline.


## Unbound

- [Unbound Config](https://gist.github.com/Overbryd/ab15ee86c58260cb6d0be634a4c58057)

Pihole + Unbound can get you DNS over TLS, DOT. This is fully encrypted DNS. Your ISP will not be able to see your DNS requests.

## Whitelist

Need somewhere to start? A robust collection of personal "white-listed" websites offered in a "by-service" structure for your consumption can be found at the root directory of this project.

My whitelist aims to be as minimal as possible, being severely tested for allowing the minimum amount of domains to go through in case of any service and sometimes directly aimed at my goals. An example of what I mean by that, would be Instagram, where I use a modified application and only use the messaging function, so I don't need domains servicing content or activity status notifications to go through. You can add those on your own.

## FAQ

1. is it better to have csv or txt lists? any difference?

### Ways to root out bad lists

- .ipset
- adblock
- .netset
- .lsrules
- .json
- .zip
- .raw
- .tar.gz


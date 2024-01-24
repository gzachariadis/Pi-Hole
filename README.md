# PiHole

## OS Selection

- [DietPi]()







## Hardening

- [Harden my pi running pihole?](https://discourse.pi-hole.net/t/harden-my-pi-running-pihole-install-ufw/5642/17)
- [Building a PiHole for Privacy and Performance](https://thesmashy.medium.com/building-a-pihole-for-privacy-and-performance-f762dbcb66e5)
- [Securing PiHole](https://discourse.pi-hole.net/t/securing-pihole/1155)

## Block Lists

- [Blocklist Tools](https://blocklist-tools.developerdan.com/blocklists)
- [Molinero.dev](https://hmirror.molinero.dev/)
- 

## Allow Lists


## Dual Setup

A second PiHole will be for redundancy, not for DNS balancing. Depending on your network and with two Pi-Holes running in parallel, the split between the two Pi-Holes is not predictable or controllable, although the first Pi-Hole listed as DNS usually receives the majority of the traffic. You won't have any control over the load balance if both Pi-Holes serve your entire network. But, you will have instant redundancy if one of the two Pi-Holes goes offline.


## Unbound
- [Unbound Config](https://gist.github.com/Overbryd/ab15ee86c58260cb6d0be634a4c58057)

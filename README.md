# PiHole

A compehensive guide to setting up my personal PiHole.

## OS Selection

- [DietPi]()
  - Lower Device Power Consumpion
  - Lean OS

## Hardening

- [Harden my pi running pihole?](https://discourse.pi-hole.net/t/harden-my-pi-running-pihole-install-ufw/5642/17)
- [Building a PiHole for Privacy and Performance](https://thesmashy.medium.com/building-a-pihole-for-privacy-and-performance-f762dbcb66e5)
- [Securing PiHole](https://discourse.pi-hole.net/t/securing-pihole/1155)

## Redundancy

### Dual Setup

A second PiHole is used for redundancy, not for DNS balancing. Depending on your network and with two Pi-Holes running in parallel, the split between the two Pi-Holes is not predictable or controllable, although the first Pi-Hole listed as DNS usually receives the majority of the traffic.

You won't have any control over the load balance if both Pi-Holes serve your entire network. But, you will have instant redundancy if one of the two Pi-Holes goes offline.

## Privacy

### Unbound

- [Unbound Config](https://gist.github.com/Overbryd/ab15ee86c58260cb6d0be634a4c58057)

Pihole + Unbound can get you DNS over TLS, DOT. This is fully encrypted DNS. Your ISP will not be able to see your DNS requests.

## Whitelist

Need somewhere to start? A robust collection of personal "white-listed" websites offered in a "by-service" structure for your consumption can be found under the Whitelist directory of this project's root folder.

My whitelist aims to serve my own personal requirements and is being severely tested to contain as few domains as possible for each service. An example of that would be not including Youtube Thumbnails domains under my Youtube.

Feel free to fork this repository and modify these lists as you see fit for your own use.

Pull requests for whitelist will only be accepted if the fix an error.

## Blacklists

### Popular

- [StevenBlack's Hosts](https://github.com/StevenBlack/hosts)
- [Hagezi's Hosts](https://github.com/hagezi/dns-blocklists/tree/main)
- [Nickoppen's Pihole Blocklist](https://github.com/nickoppen/pihole-blocklists)
- [AnudeepND Blocklist](https://github.com/anudeepND/blacklist)
- [Blocklist Project](https://github.com/blocklistproject/Lists)
- [EasyList](https://easylist.to/)
- [The Firebog](https://firebog.net/)
- [LightSwitch05](https://github.com/lightswitch05/hosts)
- [OISD](https://dbl.oisd.nl/)
- [OISD NSFW](https://dbl.oisd.nl/nsfw/)

### Social Media

- [Bolawell's Social Media Hosts](https://github.com/bolawell/Social-media-Blocklists)
- [D43m0nhLlnt3r's Social Media Hosts](https://github.com/d43m0nhLInt3r/socialblocklists)
- [Gieljnssns's Social Media Blocklist](https://github.com/gieljnssns/Social-media-Blocklists)
- [Koen20's Facebook Blocklist](https://github.com/koen20/pihole-facebook)

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

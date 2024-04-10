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

Need somewhere to start? A robust collection of personal white-listed websites offered in a by-service structure for your consumption can be found under the Whitelist directory of this project's root folder.

**BEWARE** The whitelist aims to serve my own personal requirements, and therefore is only to be used as a starting block. For example, my [Youtube](https://github.com/gzachariadis/Pi-Hole/tree/main/Whitelist/Video%20Hosting/Youtube) list, does not contain Thumbnail Domains; that's because I don't like to see Youtube Thumbnails, I find them misleading and distracting, if you disagree, just add those domains afterwards from your Query Log.

I plan to keep updating this repository, quite frequently, but feel free to fork this repository and modify these lists as you see fit for your own use.

Pull requests for whitelist will only be accepted for errors and improvements, not for additional content.

## Blacklists

I propose you select the lists of you find more useful and add them from multiple mirrors, for redudancy. Although, it will make managing them a bit tougher once they grow into many.

### Popular

- [x] [StevenBlack's Hosts](https://github.com/StevenBlack/hosts)
- [x] [Hagezi's Hosts](https://github.com/hagezi/dns-blocklists/tree/main)
- [x] [Nickoppen's Pihole Blocklist](https://github.com/nickoppen/pihole-blocklists)
- [x] [AnudeepND Blocklist](https://github.com/anudeepND/blacklist)
- [x] [Blocklist Project](https://github.com/blocklistproject/Lists)
- [ ] [EasyList](https://easylist.to/)
- [x] [The Firebog](https://firebog.net/)
- [x] [LightSwitch05](https://github.com/lightswitch05/hosts)
- [x] [OISD](https://dbl.oisd.nl/) & [OISD NSFW](https://dbl.oisd.nl/nsfw/)
- [x] [NoTracking](https://github.com/notracking/hosts-blocklists?tab=readme-ov-file)
- [x] [Just Domains](https://github.com/justdomains/blocklists)
- [x] [CombinedPrivacy](https://github.com/bongochong/CombinedPrivacyBlockLists)
- [x] [Accomplist](https://github.com/cbuijs/accomplist)

### Social Media

- [x] [Bolawell's Social Media Hosts](https://github.com/bolawell/Social-media-Blocklists)
- [x] [D43m0nhLlnt3r's Social Media Hosts](https://github.com/d43m0nhLInt3r/socialblocklists)
- [x] [Gieljnssns's Social Media Blocklist](https://github.com/gieljnssns/Social-media-Blocklists)
- [x] [Koen20's Facebook Blocklist](https://github.com/koen20/pihole-facebook)

### Apple Specific

- [x] [Apple Telemetry](https://github.com/cedws/apple-telemetry)

### Outdated

- [x] [hl2guide](https://github.com/hl2guide/Filterlist-for-AdGuard-or-PiHole?tab=readme-ov-file)

## FAQ

1. is it better to have csv or txt lists? any difference?

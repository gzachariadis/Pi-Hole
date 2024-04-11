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
- [ ] [EasyList](https://github.com/ZingyAwesome/easylists-for-pihole)
- [x] [The Firebog](https://firebog.net/)
- [x] [LightSwitch05](https://github.com/lightswitch05/hosts)
- [x] [OISD](https://dbl.oisd.nl/) & [OISD NSFW](https://dbl.oisd.nl/nsfw/)
- [x] [NoTracking](https://github.com/notracking/hosts-blocklists?tab=readme-ov-file)
- [x] [Just Domains](https://github.com/justdomains/blocklists)
- [x] [CombinedPrivacy](https://github.com/bongochong/CombinedPrivacyBlockLists)
- [x] [Accomplist](https://github.com/cbuijs/accomplist)
- [ ] [NeoDev Hosts](https://github.com/neodevpro/neodevhost)
- [ ] [Mobile Trackers](https://github.com/craiu/mobiletrackers)
- [ ] [Blockconvert](https://github.com/mkb2091/blockconvert)
- [ ] [MullVad DNS-Blocklist](https://github.com/mullvad/dns-blocklists?tab=readme-ov-file#lists)
- [ ] [jmDugan's Blocklists](https://github.com/jmdugan/blocklists)
- [ ] [1Hosts](https://github.com/badmojr/1Hosts)
- [ ] [Sefinek Blocklist](https://github.com/sefinek24/Sefinek-Blocklist-Collection)
- [ ] [ShadowWhisperer Blocklist](https://github.com/ShadowWhisperer/BlockLists)
- [ ] [Black Mirror](https://github.com/T145/black-mirror)
- [ ] [OISD NL](https://github.com/zoonderkins/dbl-oisd-nl)
- [ ] [The Ultimate Hosts Blacklist](https://github.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist)
- [ ] [hBlock](https://github.com/hectorm/hblock)
- [ ] [Spam404](https://github.com/Spam404/lists)
- [ ] [Esox-Lucius](https://github.com/Esox-Lucius/PiHoleblocklists)
- [ ] [Phising](https://phishing.army/)
- [ ] [EasyList - EasyPrivacy - Fanboy](https://github.com/easylist/easylist)
- [ ] [ShadowWhisperer](https://github.com/ShadowWhisperer/BlockLists/tree/master)

### Social Media
s
- [x] [Bolawell's Social Media Hosts](https://github.com/bolawell/Social-media-Blocklists)
- [x] [D43m0nhLlnt3r's Social Media Hosts](https://github.com/d43m0nhLInt3r/socialblocklists)
- [x] [Gieljnssns's Social Media Blocklist](https://github.com/gieljnssns/Social-media-Blocklists)
- [x] [Facebook Blocklist](https://github.com/koen20/pihole-facebook)
- [ ] [Facebook Blocklists v2](https://github.com/imkarthikk/pihole-facebook)
- [ ]

### Specific

- [x] [Apple Telemetry](https://github.com/cedws/apple-telemetry)
- [ ] [No Google](https://github.com/nickspaargaren/no-google)
- [ ] [Adobe](https://github.com/Ruddernation-Designs/Adobe-URL-Block-List)
- [ ] [Porn](https://github.com/Bon-Appetit/porn-domains)
- [ ] [Xiaomi](https://github.com/unknownFalleN/xiaomi-dns-blocklist)
- [ ] [NSA & CIA](https://github.com/tigthor/NSA-CIA-Blocklist)
- [ ] [Tik-Tok](https://github.com/danhorton7/pihole-block-tiktok)
- [ ] [Twitter](https://github.com/JackCuthbert/pihole-twitter)

### Outdated

- [x] [hl2guide](https://github.com/hl2guide/Filterlist-for-AdGuard-or-PiHole?tab=readme-ov-file)
- [ ] [EnergizedProtection](https://github.com/EnergizedProtection/block)

### Others

- [ ] [ph00lt0](https://github.com/ph00lt0/blocklist)
- [ ] [Zangadoprojets](https://github.com/zangadoprojets/pi-hole-blocklist)
- [ ] [The Great Wall](https://github.com/Sekhan/TheGreatWall)
- [ ] [Perflyst](https://github.com/Perflyst/PiHoleBlocklist)
- [ ] [Gyli](https://github.com/gyli/Blocklist)
- [ ] [Anti-Telemetry](https://github.com/MoralCode/pihole-antitelemetry)
- [ ] [Ultimate-Blocklist](https://github.com/walshie4/Ultimate-Blocklist)
- [ ] [KitsapCreator](https://github.com/KitsapCreator/pihole-blocklists)
- [ ] [Mhhakim](https://github.com/mhhakim/pihole-blocklist)
- [ ] [cNAME-Cloaking Blocking](https://github.com/nextdns/cname-cloaking-blocklist)
- [ ] [DuckDuckGo Tracker](https://github.com/duckduckgo/tracker-blocklists)
- [ ] [Lassekongo83](https://github.com/lassekongo83/Frellwits-filter-lists)
- [ ] [Piracy Blocklist](https://github.com/nextdns/piracy-blocklists)
- [ ] [Blacklist](https://github.com/fabriziosalmi/blacklists)
- [ ] [Yet another Pi-Hole List](https://github.com/JavanXD/ya-pihole-list)
- [ ] [No Qanon](https://github.com/rimu/no-qanon)
- [ ] [Scam BLocklist](https://github.com/durablenapkin/scamblocklist)
- [ ] [DonutDNS](https://github.com/shoenig/donutdns)
- [ ] [The Big List of Hacked Malware Websites](https://github.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites)
- [ ] [Notrack Blocklist](https://gitlab.com/quidsup/notrack-blocklists)
- [ ] [Scam Blocklist](https://github.com/durablenapkin/scamblocklist)
- [ ] [Smashblock](https://github.com/smashah/smashblock)
- [ ] [Emerging Threats](https://github.com/tweedge/emerging-threats-pihole)
- [ ] [PeterDaveHello - Threats](https://github.com/PeterDaveHello/threat-hostlist)
- [ ] [UrlHaus-Filter](https://github.com/curbengh/urlhaus-filter)
- [ ] [KADHosts](https://github.com/FiltersHeroes/KADhosts)
- [ ] [NoCoin Adblock](https://github.com/hoshsadiq/adblock-nocoin-list)
- [ ] [Antifa-n](https://github.com/antifa-n/pihole)

## FAQ

1. is it better to have csv or txt lists? any difference?

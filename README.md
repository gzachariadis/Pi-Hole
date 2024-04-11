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

Why so many?

- Redudancy.
- Doubles as a Firewall.
- Whitelist by Group.

### Sources

- [x] [StevenBlack's Hosts](https://github.com/StevenBlack/hosts)
- [x] [Hagezi's Hosts](https://github.com/hagezi/dns-blocklists/tree/main)
- [x] [Nickoppen's Pihole Blocklist](https://github.com/nickoppen/pihole-blocklists)
- [x] [AnudeepND Blocklist](https://github.com/anudeepND/blacklist)
- [x] [Blocklist Project](https://github.com/blocklistproject/Lists)
- [x] [EasyList](https://github.com/ZingyAwesome/easylists-for-pihole)
- [x] [The Firebog](https://firebog.net/)
- [x] [LightSwitch05](https://github.com/lightswitch05/hosts)
- [x] [OISD](https://dbl.oisd.nl/) & [OISD NSFW](https://dbl.oisd.nl/nsfw/)
- [x] [NoTracking](https://github.com/notracking/hosts-blocklists?tab=readme-ov-file)
- [x] [Just Domains](https://github.com/justdomains/blocklists)
- [x] [CombinedPrivacy](https://github.com/bongochong/CombinedPrivacyBlockLists)
- [x] [Accomplist](https://github.com/cbuijs/accomplist)
- [x] [Mobile Trackers](https://github.com/craiu/mobiletrackers)
- [x] [Blockconvert](https://github.com/mkb2091/blockconvert)
- [x] [MullVad DNS-Blocklist](https://github.com/mullvad/dns-blocklists?tab=readme-ov-file#lists)
- [x] [jmDugan's Blocklists](https://github.com/jmdugan/blocklists)
- [x] [1Hosts](https://github.com/badmojr/1Hosts)
- [x] [Sefinek Blocklist](https://github.com/sefinek24/Sefinek-Blocklist-Collection)
- [x] [ShadowWhisperer Blocklist](https://github.com/ShadowWhisperer/BlockLists)
- [x] [Black Mirror](https://github.com/T145/black-mirror)
- [x] [OISD NL](https://github.com/zoonderkins/dbl-oisd-nl)
- [x] [The Ultimate Hosts Blacklist](https://github.com/Ultimate-Hosts-Blacklist/Ultimate.Hosts.Blacklist)
- [x] [hBlock](https://github.com/hectorm/hblock)
- [x] [Spam404](https://github.com/Spam404/lists)
- [x] [Phising](https://phishing.army/)
- [x] [ShadowWhisperer](https://github.com/ShadowWhisperer/BlockLists/tree/master)
- [x] [Apple Telemetry](https://github.com/cedws/apple-telemetry)
- [x] [No Google](https://github.com/nickspaargaren/no-google)
- [x] [Adobe](https://github.com/Ruddernation-Designs/Adobe-URL-Block-List)
- [x] [Porn](https://github.com/Bon-Appetit/porn-domains)
- [x] [Xiaomi](https://github.com/unknownFalleN/xiaomi-dns-blocklist)
- [x] [NSA & CIA](https://github.com/tigthor/NSA-CIA-Blocklist)
- [x] [Tik-Tok](https://github.com/danhorton7/pihole-block-tiktok)
- [x] [Twitter](https://github.com/JackCuthbert/pihole-twitter)
- [x] [hl2guide](https://github.com/hl2guide/Filterlist-for-AdGuard-or-PiHole?tab=readme-ov-file)
- [x] [EnergizedProtection](https://github.com/EnergizedProtection/block)
- [x] [ph00lt0](https://github.com/ph00lt0/blocklist)
- [x] [Zangadoprojets](https://github.com/zangadoprojets/pi-hole-blocklist)
- [x] [The Great Wall](https://github.com/Sekhan/TheGreatWall)
- [x] [Perflyst](https://github.com/Perflyst/PiHoleBlocklist)
- [x] [Gyli](https://github.com/gyli/Blocklist)
- [x] [Anti-Telemetry](https://github.com/MoralCode/pihole-antitelemetry)
- [x] [Ultimate-Blocklist](https://github.com/walshie4/Ultimate-Blocklist)
- [x] [KitsapCreator](https://github.com/KitsapCreator/pihole-blocklists)
- [x] [Mhhakim](https://github.com/mhhakim/pihole-blocklist)
- [x] [cNAME-Cloaking Blocking](https://github.com/nextdns/cname-cloaking-blocklist)
- [x] [DuckDuckGo Tracker](https://github.com/duckduckgo/tracker-blocklists)
- [x] [Lassekongo83](https://github.com/lassekongo83/Frellwits-filter-lists)
- [x] [Piracy Blocklist](https://github.com/nextdns/piracy-blocklists)
- [x] [Blacklist](https://github.com/fabriziosalmi/blacklists)
- [x] [Yet another Pi-Hole List](https://github.com/JavanXD/ya-pihole-list)
- [x] [No Qanon](https://github.com/rimu/no-qanon)
- [x] [Scam BLocklist](https://github.com/durablenapkin/scamblocklist)
- [x] [DonutDNS](https://github.com/shoenig/donutdns)
- [x] [The Big List of Hacked Malware Websites](https://github.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites)
- [x] [Notrack Blocklist](https://gitlab.com/quidsup/notrack-blocklists)
- [x] [Scam Blocklist](https://github.com/durablenapkin/scamblocklist)
- [x] [Smashblock](https://github.com/smashah/smashblock)
- [x] [Emerging Threats](https://github.com/tweedge/emerging-threats-pihole)
- [x] [PeterDaveHello - Threats](https://github.com/PeterDaveHello/threat-hostlist)
- [x] [UrlHaus-Filter](https://github.com/curbengh/urlhaus-filter)
- [x] [KADHosts](https://github.com/FiltersHeroes/KADhosts)
- [x] [NoCoin Adblock](https://github.com/hoshsadiq/adblock-nocoin-list)
- [x] [Antifa-n](https://github.com/antifa-n/pihole)
- [ ] [EasyList - EasyPrivacy - Fanboy](https://github.com/easylist/easylist)
- [ ] [Esox-Lucius](https://github.com/Esox-Lucius/PiHoleblocklists)

## FAQ

1. is it better to have csv or txt lists? any difference?

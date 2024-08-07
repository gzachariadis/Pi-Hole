<h1>PiHole</h1>

A compehensive guide to setting up my personal configuration.

<!-- TOC -->

- [Hardware](#hardware)
  - [Operating System](#operating-system)
  - [Boot Options](#boot-options)
  - [OS Hardening](#os-hardening)
  - [Virtualization](#virtualization)
- [Configuration](#configuration)
  - [Redundancy](#redundancy)
    - [Dual Setup](#dual-setup)
    - [Mirrors](#mirrors)
  - [Privacy](#privacy)
    - [DNS Over HTTPs or DNS over TLS?](#dns-over-https-or-dns-over-tls)
  - [Networking](#networking)
    - [DHCP or Static DNS?](#dhcp-or-static-dns)
    - [Forcing DNS](#forcing-dns)
      - [Sources](#sources)
  - [Performance](#performance)
  - [Settings](#settings)
    - [Whitelist](#whitelist)
    - [Regex Blacklisting](#regex-blacklisting)
    - [Adlists](#adlists)
- [Maintenance](#maintenance)
  - [Updating](#updating)
    - [Database Update Frequency](#database-update-frequency)
- [Final Words](#final-words)

<!-- /TOC -->

# Hardware

## Operating System

- [DietPi]()
  - Lower Device Power Consumpion
  - Lean OS

## Boot Options

USB Boot

You can also choose a USB flash drive as your main drive. Using a USB as your main drive will resolve the issue of writing too many times. USB jump drives are not only more endurant but they are faster than micro SD cards.

You can use the Raspberry Pi Imager to make the Pi boot from USB. SanDisk is a good brand of USB drive to buy.

## OS Hardening

- [Harden my pi running pihole?](https://discourse.pi-hole.net/t/harden-my-pi-running-pihole-install-ufw/5642/17)
- [Building a PiHole for Privacy and Performance](https://thesmashy.medium.com/building-a-pihole-for-privacy-and-performance-f762dbcb66e5)
- [Securing PiHole](https://discourse.pi-hole.net/t/securing-pihole/1155)
- [Fail2Ban](https://github.com/mitchellkrogza/Fail2Ban-Blacklist-JAIL-for-Repeat-Offenders-with-Perma-Extended-Banning)

## Virtualization

# Configuration

## Redundancy

### Dual Setup

A second PiHole is used for redundancy, not for DNS balancing. Depending on your network and with two Pi-Holes running in parallel, the split between the two Pi-Holes is not predictable or controllable. Although, the first Pi-Hole listed as DNS usually receives the majority of the traffic.

You won't have any control over the load balance if both Pi-Holes serve your entire network. But, you will have instant redundancy if one of the two Pi-Holes goes offline.

### Mirrors

I try to create, maintain and search for mirrors for any blocklists under my configuration. That comes at a monetary cost, requiring more spacious SD cards, in my case I go for a 64gb SD, but in the future a 128gb might be required.

## Privacy

### DNS Over HTTPs or DNS over TLS?

- [Unbound Config](https://gist.github.com/Overbryd/ab15ee86c58260cb6d0be634a4c58057)

Pihole + Unbound can get you DNS over TLS, DOT. This is fully encrypted DNS. Your ISP will not be able to see your DNS requests.

<br>

Pi-hole ad blocker is great for what it does, blocking ads. But your DNS servers (eg. your ISP, Google, etc.) can and do sniff to find out what websites you are visiting (even the HTTPS sites). This is because DNS name resolutions (eg. google.com refers to this IP) are done as plain texts. In addition, this also poses some level of security risk.

DNS Over HTTPS
The solution here is to send even your DNS lookup through HTTPS protocol (encrypted). Not all DNS providers offer this (because they won't be able to track your activity). Cloudflare does provide DNS over HTTPS.

Setting up DNS over HTTPS with Pi-hole on Raspberry Pi is quite easy. It requires command-line work but it is quite easy if you follow Pi-hole documentation for DNS over HTTPS.

How can I test if DNS over HTTPS is working?

Cloudflare has a test page that will provide information on your connection. Visit this page and it will tell you where you are connecting from, which DNS resolvers you are using, and whether the connection is secure or not.

I have Pi-hole and DNS Over HTTPS, can I improve my privacy even more?

Definitely. Take a look at configuring Unbound with Pi-hole. Instead of trusting your upstream DNS (eg. Cloudflare's 1.1.1.1 or 1.0.0.1), Unbound, a recursive DNS resolver that will run locally, will connect to the responsible server directly.

This will avoid the exact path you are visiting from being logged anywhere.

DNSSEC Issue

If you decide to setup Unbound, then make sure to disable caching and DNSSEC validation. Due to some existing DNSSEC bugs in dnsmasq, the developers recommend not using Pi-hole DNSSEC with unbound or Cloudflare.

You can disable DNSSEC using the Pi-hole admin dashboard (Settings -> DNS). Disabling Pi-hole caching requires setting the cache size to 0 in /etc/dnsmasq.d/01-pi-hole.conf, as described here.

## Networking

### DHCP or Static DNS?

Disadvantages of Using Pi-hole for DNS Only

There are some disadvantages to letting your router handle DHCP while specifying preferred DNS:

Per-host tracking will be unavailable and all requests to Pi-hole will appear as if they are coming from your router. My personal opinion is that this is not a big deal for a typical home user.
You will not be able to connect to devices with their hostnames as Pi-hole cannot resolve hostnames. Again, not a big deal for a typical home user in my opinion.

If the above two disadvantages are deal breakers for you, then you can partially overcome those by using [Pi-hole Hosts file](https://discourse.pi-hole.net/t/how-do-i-show-hostnames-instead-of-ip-addresses-in-the-dashboard/3530) or fully by advertising Pi-hole's IP address via [dnsmasq](https://discourse.pi-hole.net/t/how-do-i-configure-my-devices-to-use-pi-hole-as-their-dns-server/245) in a router, if supported.

You will have to renew the DHCP leases provided by the router. The easiest way to do this is to restart the devices because resetting them locally on the device itself only updates settings for the single device. Rebooting forces the device to go offline and connect to the router again.

Alternatively, you may let your Pi-hole Server handle DHCP instead of your router, which would eliminate the disadvantages.

### Forcing DNS

#### Sources

Firewall considerations

This is beyond the scope of this tutorial, but at least worth mentioning. If you have kids that being blocked from stuff they’re searching for, or if you’re running Pi-hole in your business and your employees want to bypass your blocking attempts, by default, there’s nothing stopping them from manually adjusting their DNS settings to use a non-Pi-hole DNS server.

To help with this, you’ll need to set up some firewall rules. For instance, you may create a rule that allows DNS services on port 53 for the IP addresses of your Pi-holes, but BLOCKS port 53 everywhere else. This way – even if someone is savvy enough to manually bypass their DNS settings to get around your Pi-hole, they still won’t be able to resolve anything. Haha…gotcha sucker.

- [ ] [Force-DNS](https://labzilla.io/blog/force-dns-pihole)
- [ ] [Block Abusive Byod Devices](https://www.virtualizationhowto.com/2014/01/how-to-find-and-block-abusive-byod-devices-on-your-network/)
- [ ] [The World's Greatest Pi-Hole](https://www.crosstalksolutions.com/the-worlds-greatest-pi-hole-and-unbound-tutorial-2023/)

## Performance

1. Improving Pi-hole Performance and Life

Move query logging to RAM - protects the SD card
Query logging provides a lot of useful information as shown below. In addition, you get a lot of statistics. However, extensive writing can damage the SD card. For this reason, it is recommended to turn off query logging.

Note that this only affects the Pi-hole log and not the data that is in the long-term database.
But, what if you want to leave it on for all the useful information it provides? A good option, in this case, is to move your logs to RAM instead of SD card. So all your logs on Raspberry Pi OS operating system will be written to RAM instead of SD card, thereby prolonging the life of SD card.

Log2ram

For this, we recommend Log2ram. The GitHub page has all the information for you to get started and customize, which only takes about 5 min or less in total.

## Settings

### Whitelist

Need somewhere to start? A robust collection of personal white-listed websites offered in a by-service structure for your consumption can be found under the Whitelist directory of this project's root folder.

**BEWARE** The whitelist aims to serve my own personal requirements, and therefore is only to be used as a starting block. For example, my [Youtube](https://github.com/gzachariadis/Pi-Hole/tree/main/Whitelist/Video%20Hosting%20Services/Youtube) list, does not contain Thumbnail Domains; that's because I don't like to see Youtube Thumbnails, I find them misleading and distracting, if you disagree, just add those domains afterwards from your Query Log.

Another useful source for specific whitelists, can be found [here](https://github.com/hl2guide/Filterlist-for-AdGuard-or-PiHole/tree/master/Whitelist-Modules)

### Regex Blacklisting

### Adlists

- [ ] [Accomplist](https://github.com/cbuijs/accomplist)
- [ ] [Esox-Lucius](https://github.com/Esox-Lucius/PiHoleblocklists)
- [ ] [Chris Trackers](https://github.com/cbuijs/accomplist/tree/master/chris/trackers)

# Maintenance

## Updating

### Database Update Frequency

How frequently should I update my Pi-hole adlists?

Keeping your block lists updated frequently is key to maintaining a secure and ad-free network environment. New malicious domains and ads sources are discovered regularly, so updating your adlists <b>at least weekly</b> is a good practice.
By default, it updates once a week, every Sunday, but you can update them more frequently with the following, which will update it at 12pm every day. This can be adjusted as needed.

# Final Words

I hope this repository helped you set up the Pi-hole for a better internet browsing experience.

Happy browsing!

P.S. This is not a recommended configuration. Please, read the documentation, please...

- [ ] [Pihole Guide](https://github.com/tgjohnst/pihole-guide)
- [ ]



- [ ] [Ultimate Pi-Hole Raspberry Pi Setup: Faster Internet in 15 min](https://www.smarthomebeginner.com/pi-hole-raspberry-pi-setup-guide-2023/)
- [ ] [Pihole Local DNS Records synchronized from Active Directory](https://www.virtualizationhowto.com/2022/01/pihole-local-dns-records-synchronized-from-active-directory/)
- [ ] [Pi-Hole vs AdGuard Home for Ad Blocking – 12 Key Differences](https://www.smarthomebeginner.com/pi-hole-vs-adguard-home/)
- [ ] [Cloudflared (DoH)](https://docs.pi-hole.net/guides/dns/cloudflared/)
- [ ] [Pi-hole as All-Around DNS Solution](https://docs.pi-hole.net/guides/dns/unbound/)
- [ ] [DNS cache](https://docs.pi-hole.net/ftldns/dns-cache/)
- [ ] [How to Run PiHole in Docker on Ubuntu, w/ and w/o Reverse Proxy?](https://www.smarthomebeginner.com/run-pihole-in-docker-on-ubuntu-with-reverse-proxy/)
- [ ] [Gravity Sync](https://github.com/vmstan/gravity-sync)
- [ ] [Configuring PiHole to Update More Regularly](https://www.bentasker.co.uk/posts/blog/privacy/467-configuring-pi-hole-to-update-blocklists-more-regularly.html)
- [ ] [Whitelisted Domains](https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212)
- [ ] [One One One One](https://one.one.one.one/help/)
- [ ] [DNS over HTTPS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/#main)
- [ ] 
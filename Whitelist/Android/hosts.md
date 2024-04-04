# Android

## Connectivity Check

This method checks whether mobile is connected to internet and returns true if connected. The reason I whitelist it, it's because in unrooted devices, some apps require it to function; [example](https://github.com/AntennaPod/AntennaPod/issues/6899#issuecomment-1913233071)

```
connectivitycheck.gstatic.com
```

In case problem persists, try whitelisting

```
android.clients.google.com
```

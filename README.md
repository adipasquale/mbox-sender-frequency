# Mbox Sender Frequency

This very small tool will display mail counts grouped by sender. This is helpful to identify automated notification mails that you may want to delete from your mailbox to free up some space.

If you're curious, I wrote a [blogpost](https://blog.dipasquale.fr) in which I explain the context in which I needed this script, namely to leave GMail.

## Usage

Clone this repo somewhere or download the standalone python script. You can then simply use it with :

```
python list_senders.py [-h] [--threshold THRESHOLD] [--group-by-email]
                       mbox_path
```

for example :

```
python3 list_senders.py --group-by-email --threshold 30 ~/Downloads/mbone.mbox
```

## Getting your mbox file from GMail

Head to [Google Takeout](https://takeout.google.com), select Mails, and opt for the file download link version. Then be patient, and you will receive a mail with a link to your own mbox file within a few hours / days.

## Limitations

This was not optimized at all, so it may be quite slow, however it ran on my 4GB file within a few minutes, which was acceptable to me.
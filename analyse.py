import re

def parse_net_pl(s):
    ret = float(re.search(r"[\-]?\$[0-9\.]+",s.replace(",","")).group().replace("$",""))
    return ret

if __name__ == "__main__":
  print "reading file"
  f = open ("tradings")
  tagline = f.readline()

  tags = [] # array of strings
  tags_stoi = {}
  trades = [] # string of arrays of trades

  for (i,x) in enumerate(tagline.split()):
      #print 'tag %d: %s' % (i,x)
      tags.append(x)
      tags_stoi[x] = i

  print "tagline read successfully"
  lines = f.readlines()
  for line in lines:
      splitted = line.split()
      inst_start = tags_stoi["Instrument"];
      inst_name = ''
      i = inst_start
      while (splitted[i] not in ["Buy", "Sell", "Long", "Short"]):
          #print "splitted[%d] {%s}" % (i, splitted[i])
          inst_name += splitted[i]
          if (i != 0):
              inst_name += " "
          i += 1
      splitted = splitted [:inst_start] + [inst_name] +  splitted [i + 1 : ]
      trades.append(splitted)
  print "trades read successfully"

  insts_trades = {} # array of instructment name to array of index into the trades array
  insts = []
  for (i,x) in enumerate(trades): 
      inst = x[tags_stoi["Instrument"]]
      if inst not in insts: 
        insts.append(inst)
        insts_trades[inst] = []
      insts_trades[inst].append(i)
  print "Instruments: %s" % insts
  total_net_pl = 0.0
  for inst in insts:
    print '==%s==' % inst
    inst_trades = insts_trades[inst] 
    n_trades = len(inst_trades)
    inst_net_pl = 0
    for trade_id in inst_trades: 
      trade = trades[trade_id]
      inst_net_pl += parse_net_pl(trade[-1])
      total_net_pl += parse_net_pl(trade[-1])
    print "Net P/L $ %.2f over %d trades" % (inst_net_pl, n_trades)
  print "Total Net P/L %.2f" % (total_net_pl)
    

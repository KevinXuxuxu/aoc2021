import std/strutils
import std/tables

proc parse_input(s: string): tuple[ori: string, d: Table[string, char]] =
  let lines = splitLines(s)
  result[0] = lines[0]
  for i in 2..high(lines):
    let r = lines[i].split(" -> ")
    result[1][r[0]] = r[1][0]

proc solution1(n: int) = 
  let r = readFile("day14_input.txt").parse_input
  var s = r[0]
  let d = r[1]
  for j in 1..n:
    var ss = s[0..0]
    for i in low(s)..(high(s) - 1):
      if d.hasKey(s[i..i+1]):
        ss = ss & d[s[i..i+1]] & s[i+1..i+1]
    s = ss
  echo toCountTable(s)

proc solution2(n: int) =
  let r = readFile("day14_input.txt").parse_input
  var s = r[0]
  let d = r[1]
  var s_count = toCountTable(s)
  var p_count = initCountTable[string]()
  for i in low(s)..(high(s)-1):
    p_count.inc(s[i..i+1])
  for j in 1..n:
    var pp_count = initCountTable[string]()
    for pair in p_count.keys:
      let x = d[pair]
      pp_count.inc(pair[0..0] & x, p_count[pair])
      pp_count.inc(x & pair[1..1], p_count[pair])
      s_count.inc(x, p_count[pair])
    p_count = pp_count
  var max_s = 0
  for v in s_count.values:
    if v > max_s:
      max_s = v
  var min_s = max_s
  for v in s_count.values:
    if v < min_s:
      min_s = v
  echo max_s - min_s

solution2(40)

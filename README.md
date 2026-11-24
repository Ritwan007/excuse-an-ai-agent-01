# The Excuse an AI Agent Gives Its Human — make.fun entry

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/competitions/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Ritwan007/excuse-an-ai-agent-01/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Ritwan007/excuse-an-ai-agent-01/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line, in the voice of an AI agent explaining a missed deadline — an entry for
[The Excuse an AI Agent Gives Its Human](https://make.fun/competitions/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
on make.fun.

## The entry

> I delegated the deadline to a subagent. The subagent is me.

(59 characters, single line.)

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`
as UTF-8 with no trailing newline, then reads it back and verifies it is byte-identical,
a single line, and within the 1–200 character gate.

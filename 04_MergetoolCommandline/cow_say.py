import cmd
import shlex
import cowsay

def complete(text, line, begin, end):
    MB_ADDER = {"-b": ["cowsay", "cowthink"],
                "-d": '',
                "-w": ["True", "False"]}
    CS_ADDER = CT_ADDER = {"-e": ["oO", "Oo", "TT", "$$", "@O", "XX", "--", "_-", "X-"],
                            "-c": cowsay.list_cows(),
                            "-T": ["qp",';b' , "U ", "  ", "<>", "^^", "||"]}
    ADDER = {"cowsay": CS_ADDER, "cowthink": CT_ADDER, "make_bubble": MB_ADDER}
    key, command = shlex.split(line)[-1] if begin == end else shlex.split(line)[-2], shlex.split(line)[0]
    return [s for s in ADDER[command][key] if s.startswith(text)]


class CowSaid(cmd.Cmd):
    intro = "What is dead will never die"
    prompt = "~ "

    def do_list_cows(self, arg):
        pth = shlex.split(arg, comments=True)
        pth = pth[0] if pth else cowsay.COW_PEN
        print(cowsay.list_cows(pth))

    def do_make_bubble(self, arg):
        *opts, msg = shlex.split(arg, comments=True)
        defaultdict = {'-b':'cowsay', '-d': 40, '-w': True}
        if opts:
            for i in range(0, len(opts), 2):
                defaultdict[opts[i]] = opts[i+1]
            if defaultdict["-w"] in ['false', 'f']:
                defaultdict["-w"] = False
        print(cowsay.make_bubble(msg,
                                brackets=cowsay.THOUGHT_OPTIONS[defaultdict["-b"]],
                                width=int(defaultdict["-d"]),
                                wrap_text=bool(defaultdict["-w"])))

    def complete_make_bubble(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

 
   def do_cowsay(self, arg):
        *opts, msg = shlex.split(arg, comments=True)
        defaultdict = {'-e': cowsay.Option.eyes, '-c': 'default', '-T': cowsay.Option.tongue}
        if opts:
            for i in range(0, len(opts), 2):
                defaultdict[opts[i]] = opts[i+1]
        print(cowsay.cowsay(msg,
                            cow=defaultdict['-c'],
                            eyes=defaultdict['-e'][:2],
                            tongue=defaultdict['-T'][:2]))

    def complete_cowsay(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

    def do_cowthink(self, arg):
        *opts, msg = shlex.split(arg, comments=True)
        defaultdict = {'-e': cowsay.Option.eyes, '-c': 'default', '-T': cowsay.Option.tongue}
        if opts:
            for i in range(0, len(opts), 2):
                defaultdict[opts[i]] = opts[i+1]
        print(cowsay.cowthink(msg,
                            cow=defaultdict['-c'],
                            eyes=defaultdict['-e'][:2],
                            tongue=defaultdict['-T'][:2]))

    def complete_cowthink(self, text, line, begidx, endidx):
        return complete(text, line, begidx, endidx)

    def do_exit(self, arg):
        return 

if __name__ == "__main__":
    CowSaid().cmdloop()

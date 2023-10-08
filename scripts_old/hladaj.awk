BEGIN {
    FS=","
}

{
    if (!(string))
        {
        print "Usage:";
        print "awk -v string=search_string -f hladaj.awk clean4_literatura.csv";
        exit(1)
        }
    else
        {
        i=1;
        while (i <= NF)
        {
            if ( tolower($i) ~ tolower(string) )
            {
            print $0
            num_match++
            break;
            }
        i++
        }
    }
}

END {
    print num_match, "of match, for", string"."
}


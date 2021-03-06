<?php

$DOCROOT = $_SERVER['DOCUMENT_ROOT'] ? $_SERVER['DOCUMENT_ROOT'] : $DOCUMENT_ROOT;
#
# On Windows servers, you may need to set $DOCROOT manually.  Check the
# PATH_TRANSLATED environment variable to see what the path should be.
# You can run the  phpinfo()  function to see that variable's value.

$DOCROOT = preg_replace("/(.+)\/$/", '$1', $DOCROOT); # remove any trailing slash.

# Change only the following 2 lines, to match the path & name of your CGI script.
# But in most cases the defaults work fine, so try them first.  And even if you do
# need to adjust $cgi_script_full, you should usually still leave $cgi_script_local
# set to the default value.
#
$cgi_script_full  = "$DOCROOT/cgi-bin/filechucker.cgi";
$cgi_script_local = "/cgi-bin/filechucker.cgi";

if(!(file_exists($cgi_script_full)))
{
	print "Error: the file specified by \$cgi_script_full does not exist ('$cgi_script_full').  You may need to edit your call_fc.php file and manually set the \$DOCROOT and/or \$cgi_script_full variables.  (\$DOCROOT is currently '$DOCROOT'.)";
	exit;
}

reset($_SERVER);
while (list ($header, $value) = each ($_SERVER))
{
	if($header == "SCRIPT_NAME" || $header == "SCRIPT_URL")
	{
		putenv("$header=$cgi_script_local");
	}
	elseif($header == "SCRIPT_FILENAME")
	{
		putenv("$header=$cgi_script_full");
	}
	elseif($header == "SCRIPT_URI")
	{
		$value = str_replace($_SERVER['SCRIPT_URL'], $cgi_script_local, $value);
		putenv("$header=$value");
	}
	else
	{
		putenv("$header=$value");
	}
}

# In case another call_foo.php has set the query-string to something
# specific for its own purposes, reset it for us:
#
$qs = $_ENV['QUERY_STRING'] ? $_ENV['QUERY_STRING'] : $_SERVER['QUERY_STRING'];
if(isset($custqs)) { $qs .= $qs ? "&" : ""; $qs .= $custqs; }
putenv("QUERY_STRING=encembed=yes&" . $qs);

unset($output);
exec($cgi_script_full, $output, $return_val);
if(!$output)
{
	exec("perl $cgi_script_full", $output, $return_val);
}

$html_headers_finished = 0;
foreach ($output as $line)
{
	if($html_headers_finished)
	{
		print "$line\n";
	}
	else
	{
		if($line == '')
		{
			$html_headers_finished = 1;
		}
	}
}

# Now unset these so as not to confuse any other CGI scripts
# that we call after this one on the same page:
#
reset($_SERVER);
while (list ($header, $value) = each ($_SERVER))
{
	$status = putenv($header) ? 'succeeded' : 'failed';
	#print "<!-- $status unsetting var $header -->\n";
}

?>

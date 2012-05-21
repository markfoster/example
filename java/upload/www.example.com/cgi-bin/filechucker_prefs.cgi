############################################################################
#
# filechucker_prefs.cgi - trial version
# Version: 4.56t-e07
# Edit the settings in this file to customize FileChucker for your needs.
# And make sure to read the FAQ: http://encodable.com/filechucker/faq
#
############################################################################
#
# NOTE: do not spend too much time customizing this trial version,
# because the full version replaces it completely.
# 
############################################################################
#
# PREFs Table of Contents:
#
# PREFs Section 01: Debugging.
# PREFs Section 02: Paths and Directories.
#
#   *Note: stop here and get the script running before customizing anything else.
#
# PREFs Section 03: Security.
# PREFs Section 04: User-directories.
# PREFs Section 05: Subdirectories.
#
#   *Note: User-directories and subdirectories are two separate things.
#
# PREFs Section 06: Email Notification.
# PREFs Section 07: Upload Form Configuration.
# PREFs Section 08: Upload Restrictions.
# PREFs Section 09: Processing Uploads.
# PREFs Section 10: Post-Upload.
# PREFs Section 11: File-List Configuration.
# PREFs Section 12: Database Setup.
# PREFs Section 13: Internationalization and Localization.
# PREFs Section 14: Templates.
# PREFs Section 15: Image Options.
# PREFs Section 16: Styling.
# PREFs Section Z:  Misc Settings Not Usually Needed.
#
############################################################################








# PREFs Section 01: Debugging.
############################################################################
# The enable_debug PREF prints some debugging output in an HTML comment at
# the bottom of the page, if you pass "debug" as the query-string.  You may
# want to enable this until you get FileChucker working properly, and then
# disable it.
#
$PREF{enable_debug}					= 'no';









# PREFs Section 02: Paths and Directories.
############################################################################
# We'll detect your server's document-root automatically, but on some
# servers you may need to uncomment this and specify it manually.  IIS users
# may need to set it like this:
#
#	$PREF{DOCROOT} = 'c:\inetpub\wwwroot';
#
#$PREF{DOCROOT}						= $ENV{DOCUMENT_ROOT};



# PREFs Section 02: Paths and Directories.
############################################################################
# The uploaded_files_dir is where the uploaded files will go.  It must be
# world-readable and world-writable, aka "chmod a+rwx" or "chmod 0777".
#
# On most servers this will be in the DOCROOT, in which case we'll prepend
# your DOCROOT to whatever you set uploaded_files_dir to.  If for some
# reason you want to specify it with an absolute path, or a path that's
# relative to the current directory instead of the DOCROOT, then set the 
# _is_in_docroot PREF to no.
#
# You can adjust various other paths here too.
#
$PREF{uploaded_files_dir}				= '/upload/files';
$PREF{uploaded_files_dir_is_in_docroot}			= 'yes';
$PREF{path_to_filelist_images}				= '/upload/fc_icons_etc/';
$PREF{human_test_image_directory___url}			= '/upload/files/fcht';
$PREF{human_test_image_directory___real}		= '%PREF{DOCROOT}/upload/files/fcht';



# PREFs Section 02: Paths and Directories.
############################################################################
# If you set uploaded_files_dir to a path outside your webspace, then we 
# won't be able to directly link to the files from your website, because
# they aren't in the DOCROOT.  If you're doing something like manually
# moving the files to somewhere else within your DOCROOT afterwards, then 
# enter that path here.  Otherwise just leave this commented out.  Note:
# don't include an ending slash on this.
#
#$PREF{uploaded_files_urlpath}				= '';



# PREFs Section 02: Paths and Directories.
############################################################################
# This is our working directory.  This must be world-readable and
# world-writable (aka "chmod a+rwx" or 0777).  By default, we set its
# _in_docroot PREF to 'no' because by default the data directory gets placed
# at the same location as the filechucker.cgi script itself, so we don't
# need to prepend the value of DOCROOT onto it; we can access it directly
# since it's in the same dir we're running in.  The default settings are:
#
#	$PREF{datadir}			= 'encdata';
#	$PREF{datadir_is_in_docroot}	= 'no';
#
# Alternatively you can set it with an absolute path, like this:
#
#	$PREF{datadir}			= '/var/www/example.com/cgi-bin/encdata';
#	$PREF{datadir_is_in_docroot}	= 'no';
#
# Or this:
#
#	$PREF{datadir}			= 'c:\inetpub\wwwroot\cgi-bin\encdata';
#	$PREF{datadir_is_in_docroot}	= 'no';
#
$PREF{datadir}						= 'encdata';
$PREF{datadir_is_in_docroot}				= 'no';



# PREFs Section 02: Paths and Directories.
############################################################################
# If you want to access FileChucker at a short URL like yoursite.com/upload/
# instead of yoursite.com/cgi-bin/filechucker.cgi, then you can do the 
# following:
#
# If you're using SSI (Apache and IIS both support this), then put the 
# following line into /upload/index.shtml on your server:
#
#	<!--#include virtual="/cgi-bin/filechucker.cgi?$QUERY_STRING" -->
#
# Or if your server runs PHP, you can put the following line into 
# /upload/index.php on your server:
#
#	<?PHP virtual("/cgi-bin/filechucker.cgi"); ?>
#
# Then set the 'here_' PREFs like this:
#
#	$PREF{here_uploader} = '/upload/';
#	$PREF{here_filelist} = '/upload/';
#	...
#
# Otherwise leave these set to $ENV{SCRIPT_NAME}.
#
# Note that in most cases these should all be set to the same value, i.e.
# unless you've actually set up multiple short URLs to point to the CGI
# script.  And if you only set the single $PREF{here} value, then the
# others will automatically be set to that value.
#
#$PREF{here}						= '/upload/';
#
$PREF{here}						= $ENV{SCRIPT_NAME};
#$PREF{here_uploader}					= $ENV{SCRIPT_NAME};
$PREF{here_popupstatus}					= $ENV{SCRIPT_NAME}; # this should be $ENV{SCRIPT_NAME} in most cases.
#$PREF{here_uploadcomplete}				= $ENV{SCRIPT_NAME};
#$PREF{here_filelist}					= $ENV{SCRIPT_NAME};
#$PREF{here_login}					= $ENV{SCRIPT_NAME};
#$PREF{here_error}					= $ENV{SCRIPT_NAME};









# PREFs Section 03: Security.
############################################################################
# Password Protection, Option 1 of 5 (simple; no usernames):
#
# If you want to require just passwords (without usernames) for access to
# the application, then you can set these hashes.  Go to:
#
#	yoursite.com/cgi-bin/filechucker.cgi?newpw
#
# Enter the password you want to use into that page, and it will generate a
# "hash" of the password, which is a string that looks something like this:
#
#	cdfc81932491375c34c842bcebc7dc15
#
# Copy and paste the hash into one of the following preferences.  Then when
# you want to log in, enter the password, not the hash.  This is so that we
# don't store the actual password on disk, which would be very insecure.
#
# We specify two possible user-levels (or "groups"): member and admin.
# (Actually, there are three, including "public" which obviously has no
# password.)  If you want, you can use just one of them, and have a single
# password for all features of the application.  Or you can specify both,
# and set the "groups_allowed_to" preferences accordingly, so that certain
# features are only available to the specified group.
#
# Admins are automatically members too, so someone with an admin password
# automatically has access to anything that requires a member password.
#
$PREF{member_password_hash_01}				= '';
$PREF{admin_password_hash_01}				= '';



# PREFs Section 03: Security.
############################################################################
# Password Protection, Option 2 of 5 (full-featured; unlimited usernames):
#
# If you need a full-featured login system (with unlimited usernames, each 
# having its own password, and unlimited groups), instead of this script's
# simple built-in password system which has just passwords without
# usernames, then you should use our UserBase application:
#
#	http://encodable.com/userbase/
#
# FileChucker integrates fully with UserBase, and if you set the PREF
# "enable_userdirs" below, then each of your users will have their own 
# private upload subdirectory.
# 
# There are 2 ways to enable UserBase integration: the original way using the
# $PREF{integrate_with_userbase} setting, and the alternative way using the
# $PREF{integrate_with_userbase_method_b} setting.  Method B should generally
# only be used when the original method fails, which may happen due to
# incompatibilities if you're running a newer version of one app and an older
# version of the other.
#
###
#
# UserBase original method and settings:
#
$PREF{integrate_with_userbase}				= 'no';
$PREF{userbase_prefs_file_basename}			= 'userbase'; # don't change this unless you've renamed your userbase_prefs.cgi file.
#
# UserBase method B and settings:
#
$PREF{integrate_with_userbase_method_b}			= 'no';
$PREF{userbase_local_scriptname}			= "/cgi-bin/userbase.cgi";
$PREF{path_to_userbase}					= "%PREF{DOCROOT}%PREF{userbase_local_scriptname}";
#
# UserBase shared settings -- for both the original method and method B: most
# of these can be left at their default values, though if you've set up the
# short /login/ URL on your site (see UserBase homepage for instructions)
# then you'll want to set login_url (but NOT logout_url) to "/login/".
#
$PREF{login_url}					= '/cgi-bin/userbase.cgi';
$PREF{logout_url}					= '/cgi-bin/userbase.cgi?logout';
$PREF{userbase_login_error_message}			= "Authentication required: please %%login_link%% first.";
$PREF{forced_logout_link}				= qq`<script type="text/javascript">location.href="%%logout_url%%";</script><p>Logging out; <a href="%%logout_url%%">click here</a> if you see this message for more than a few seconds.</p>\n`;
$PREF{loggedout_page_template__no_referer}		= qq`You are logged out.`;
$PREF{loggedout_page_template__with_referer}		= qq`<p>You are logged out.&nbsp; <a href="%%ref%%">Click here</a> to return to the page you came from.</p>`;
$PREF{login_status_string_template}			= qq`[ %%usertype%% %%username%% logged in%%extra_info%%. ]`;
$PREF{needlogin_message}				= qq`%%js_auto_redirect%%<h1 class="pagetitle">Login Required</h1><p>Login required; <a href="%%login_url%%">click here</a> to continue.</p>`;
$PREF{needprivs_message}				= qq`%%js_auto_redirect%%<h1 class="pagetitle">Access Denied</h1><p>Access denied.&nbsp; %%%if-notloggedin%%%Perhaps you need to <a href="%%login_url%%">login</a> first?%%%end-notloggedin%%%</p>`;



# PREFs Section 03: Security.
############################################################################
# Password Protection, Option 3 of 5 (use your site's existing login system):
#
# If your site already has a login system, either cookie-based or based on
# PHP sessions, you can make FileChucker integrate with it.
#
# If using the PHP session method, you must set the following environment
# variables from PHP just before calling filechucker.cgi from PHP:
#
# 	putenv("PHP_ENC_USERNAME=$username");	# where $username is your PHP user variable.
# 	putenv("PHP_ENC_ISADMIN=$X");		# where $X is a 0 or a 1.
#
# This option is mutually exclusive with the integrate_with_userbase option.
#
$PREF{integrate_with_existing_login_system}		= 'no';
$PREF{login_error_message}				= qq`Error: not logged in.&nbsp; Perhaps you need to <a href="/">go home</a> and log in first?`;
#$PREF{logout_url}					= '/logout/';
#$PREF{login_url}					= '/login/';
#$PREF{forced_logout_link}				= qq`<p>Logging out; <a href="%%logout_url%%">click here</a> to continue.</p>\n`;
#
$PREF{enable_username_from_cookie}			= 'no';
$PREF{member_username_cookie_name}			= 'member_username';
$PREF{admin_username_cookie_name}			= 'admin_username';
#
$PREF{enable_username_from_php_session}			= 'no';



# PREFs Section 03: Security.
############################################################################
# (Pseudo-)Password Protection, Option 4 of 5 (automatic private directories):
#
# You can enable this serial_is_userdir option to get much of the benefit
# of usernames & passwords without actually having to use usernames or
# passwords.  When configured this way, FileChucker will automatically put
# each new upload into a new unique private subdirectory, something like:
#
#	yoursite.com/upload/?userdir=11832920981234098203458234098123
#
# This is primarily meant to facilitate single-use uploads, for instance
# where a person just wants to share one file one time; however by using
# the link provided at the end of the upload and in the notification email,
# the user can actually reuse the same uploads folder for as long as he wishes.
#
# In order to configure FileChucker this way, in addition to setting this
# serial_is_userdir PREF, you should also find & set the following:
#
#	$PREF{serial_is_userdir}				= 'yes';
#	$PREF{enable_userdirs}					= 'yes';
#	$PREF{keep_userdir_on_url}				= 'yes';
#	$PREF{enable_userdir_on_url}				= 'yes';
#	$PREF{error_if_userdir_not_supplied}			= 'yes';
#	$PREF{auto_create_userdirs}				= 'yes';
#	$PREF{groups_allowed_to_upload}				= 'public';
#	$PREF{groups_allowed_to_list_files}			= 'public';
#	$PREF{groups_allowed_to_download}			= 'public';
#	$PREF{groups_allowed_to_delete_items}			= 'public';
#	$PREF{hide_path_to_uploads_dir}				= 'yes';
#	$PREF{enable_subdirs}					= 'yes';
#	$PREF{display_dropdown_box_for_subdir_selection}	= 'no';
#	$PREF{navigate_users_into_userdirs_automatically}	= 'yes';
#	$PREF{hide_links_to_topmost_level_from_userdir_users}	= 'yes';
#	$PREF{enable_manual_creation_of_new_subdirs_during_upload}= 'no';
#
# If you'd rather not go through all the PREFs trying to find those, you
# can copy that block of PREFs from here, and paste it at the very bottom
# of this prefs file (be sure to uncomment each line by deleting the "#"
# from the start of the line).
#
# When one of your users first visits FileChucker, it will automatically
# redirect them to the same page but with ?userdir=NNNNNNNNNN... on the URL.
# If this redirection causes problems for your page, which generally should
# not happen except in some complex embedded installations, then you can
# disable the $PREF{error_if_userdir_not_supplied} setting.  This has the
# side-effect of creating an empty userdir each time FileChucker runs, even
# if the visitor doesn't upload any files, so you'll end up with some empty
# folders in your userdirs directory.
#
$PREF{serial_is_userdir}				= 'no';



# PREFs Section 03: Security.
############################################################################
# Password Protection, Option 5 of 5 (per-file passwords):
# 
# You can set an individual password on each uploaded file, by specifying
# the password during the upload process.  This password-protection option
# actually works in addition to any of the other password-protection options
# that you specify above.  To enable it, create 2 formfields on the upload
# form by creating the following prefs at the end of PREFs Section 07:
# 
#	$PREF{formfield_01}		= "Password for this file:";
#	$PREF{formfield_01_password}	= 'yes';
#	$PREF{formfield_01_shortname}	= 'filepw';
#	
#	$PREF{formfield_02}		= "Password, again:";
#	$PREF{formfield_02_password}	= 'yes';
#	$PREF{formfield_02_shortname}	= 'filepwverify';
#
# See the formfield documentation at the end of PREFs Section 07 for more
# details on formfields in general.  For these particular formfields, it's
# OK to adjust their number (01, 02) and the text that's displayed, but
# don't change their shortnames.
#
# This feature requires that the $PREF{store_upload_info_in_database}
# setting be enabled in PREFs Section 09.
#
$PREF{enable_perfile_passwords}				= 'no';



# PREFs Section 03: Security.
############################################################################
# Whether you're using UserBase or FileChucker's built-in password system,
# the following "groups_allowed_to_*" PREFs control who can access what.
# Each item must be set to a comma-separated list of group names.  If you're
# not using UserBase, then the only possible groupnames are public, member,
# and admin.  Note that public includes member and admin (i.e. members and
# administrators are also members of the public), and member includes admin
# (i.e. administrators are also members).
#
# For each of the groups_allowed_to_action settings here, you can also 
# create a new setting called groups_not_allowed_to_action, which works
# the same way but in reverse: it explicitly disallows the action.
#
# If you are customizing FileChucker by modifying its internal code, and you
# want to add your own restricted actions here, see the user_is_allowed_to()
# function, and search the script for calls to that function, to see how the
# system works.
#
$PREF{groups_allowed_to_upload}				= 'public';
$PREF{groups_allowed_to_list_files}			= 'public';
$PREF{groups_allowed_to_list_files_in_top_level}	= 'public';
$PREF{groups_allowed_to_view_all_userdirs}		= 'admin';
$PREF{groups_allowed_to_download}			= 'public';
$PREF{groups_allowed_to_view_upload_info}		= 'public';
$PREF{groups_allowed_to_view_administration_page}	= 'admin';
#
$PREF{groups_allowed_to_view_upload_log_db}		= 'admin';
$PREF{groups_allowed_to_edit_upload_log_db}		= 'admin';
$PREF{groups_allowed_to_delete_upload_log_db_records}	= 'admin';
$PREF{groups_allowed_to_view_download_log_db}		= 'admin';
$PREF{groups_allowed_to_edit_download_log_db}		= 'admin';
$PREF{groups_allowed_to_delete_download_log_db_records}	= 'admin';
#
$PREF{groups_allowed_to_view_options_menus_on_filelist}	= 'public';
$PREF{groups_allowed_to_copy_items}			= 'public';
$PREF{groups_allowed_to_move_items}			= 'public';
$PREF{groups_allowed_to_delete_items}			= 'public';
$PREF{groups_allowed_to_replace_existing_files}		= 'public';
$PREF{groups_allowed_to_reprocess_existing_files}	= 'public';
$PREF{groups_allowed_to_order_items}			= 'public';
$PREF{groups_allowed_to_force_update_of_thumbs_cache}	= 'public';
$PREF{groups_allowed_to_choose_subdir_during_upload}	= 'public';
$PREF{groups_allowed_to_create_folders_during_upload}	= 'public';
$PREF{groups_allowed_to_create_folders_thru_filelist}	= 'public';
$PREF{groups_allowed_to_rotate_images}			= 'public';




# PREFs Section 03: Security.
############################################################################
# Once you allow someone to download a file from your uploads area,
# they will know the path to all your uploads.  If you don't want
# them to be able to see all the other files by just visiting that
# directory's address, you'll need to put a .htaccess file in that
# directory with the line "Options -Indexes" (without quotes).
# However, as long as they know the address, they can still try to
# guess filenames that might be in there.  As an extra security
# precaution, you can set serialize_all_uploads, which adds a long
# pseudo-random number to each filename, making it virtually
# impossible that someone could guess the name of a file in the
# directory.
#
$PREF{serialize_all_uploads}				= 'no';



# PREFs Section 03: Security.
############################################################################
# Choose whether the script should display a link to the list of
# uploaded files.  Note that "members" includes "admins", and
# "strangers" includes everyone (i.e. members and admins too).
#
$PREF{show_link_to_uploads_for_strangers}		= 'yes';
$PREF{show_link_to_uploads_for_members}			= 'yes';
$PREF{show_link_to_uploads_for_admins}			= 'yes';



# PREFs Section 03: Security.
############################################################################
# If you're running an HTTPS server, and you want FileChucker to always
# use secure links, change this to https://.  But note that this only
# affects links generated by FileChucker itself; it doesn't prevent your
# users from typing http:// (without the "s") into their address bar.
# For that, you'll need to enable $PREF{force_https}.
# 
$PREF{protoprefix}					= 'http://';
$PREF{force_https}					= 'no';



# PREFs Section 03: Security.
############################################################################
# When an upload finishes, we display an "Upload Complete" page, which
# lists the names of the files that were uploaded, along with their
# sizes, and some other information.  On this page, each filename is a
# link to download that file, unless you set these to 'no'.
#
$PREF{upload_complete_page_links_to_files_for_strangers}= 'yes';
$PREF{upload_complete_page_links_to_files_for_members}	= 'yes';
$PREF{upload_complete_page_links_to_files_for_admins}	= 'yes';



# PREFs Section 03: Security.
############################################################################
# Whether to display the login link in the footer-links at the bottom of
# the page.  If you don't want to display it, then you log in by either
# trying to access a page you don't have access to (which will print the
# login link in the error message), or by passing ?login to the script.
# Of course if you're not configuring your FileChucker with any of the
# password PREFs then this is irrelevant.
#
$PREF{show_login_link}					= 'yes';



# PREFs Section 03: Security.
############################################################################
# In various places -- the upload subdirectory drop-down box, the move-item
# page, etc -- we need to show the user a path to the uploaded files.  The
# beginning of this path will be the value of your uploaded_files_dir if
# that's in your docroot, or else it'll be the value you set for
# uploaded_files_urlpath.  But if you want that beginning part of the path
# to be hidden from your users, then enable this PREF.  Note that the user
# can still see this part of the path whenever they actually download a
# file, since naturally we need to go through the whole path to get to the
# file.
#
$PREF{hide_path_to_uploads_dir}				= 'no';



# PREFs Section 03: Security.
############################################################################
# The human test is meant to prevent spambots or other evil people/systems
# from hammering on your uploader.  It asks a question that should be easy
# for a person to answer, but difficult for a computer to answer.  Currently
# this means displaying an image containing random characters and asking the
# user to type those characters into an input field.
#
# This type of test is sometimes called a CAPTCHA; this term is trademarked
# by Carnegie Mellon University.
#
# If you want to use this feature, you should start by using the invisible
# mode (human_test_is_invisible).  This method relies on the fact that
# Javascript is not supported by the various nastybots that will abuse your
# site, so we use Javascript to hide the human test and fill in the correct
# answer automatically, thereby not requiring any actual human involvement.
# But, if the nastybots are still getting through, then try enable_human_test
# without the invisible option.
#
# The image directory must be world-writable (0777) and within the DOCROOT
# but not inside the cgi-bin.
#
# The default salt value is probably fine.  If your site is getting
# successfully hammered despite the human test being enabled, changing
# the salt periodically may help.
#
# You probably want to automatically delete the test images after a little
# while.  The schedule for this (daily/hourly/minutes/etc) uses the same 
# values from the delete_old_* feature in PREFs Section 11, except for
# the max age.
#
$PREF{enable_human_test}				= 'no';
$PREF{human_test_is_invisible}				= 'yes';
$PREF{human_test_num_digits}				= 6; # from 1 to 15.
$PREF{human_test_salt_value}				= substr($ENV{HTTP_HOST}, 0, 5);
$PREF{automatically_delete_old_humantest_images}	= 'yes';
$PREF{max_age_for_humantest_images}			= '1'; # In hours, but can be fractional (decimal).
$PREF{human_test_image_width}				= '80';
$PREF{human_test_image_height}				= '24';
$PREF{human_test_font_name}				= 'Helvetica'; # Try Helvetica, Courier, Arial, etc.  Currently ImageMagick-only.
$PREF{human_test_text_size}				= '18'; # Note: has no effect on some GD-only servers.
$PREF{human_test_text_color}				= 'black';
$PREF{human_test_background_color}			= 'white';
$PREF{human_test_border_size}				= '1';
$PREF{human_test_border_color}				= 'gray';
$PREF{human_test_margin}				= '5px';




# PREFs Section 03: Security.
############################################################################
# We should only accepts posts (uploads) from ourself, and optionally any
# other URLs that you specify here.  The only reason you should specify
# any other URLs is if you're hosting the upload form on a different site
# than the CGI script.
#
# Note: this feature is still somewhat experimental, as a small percentage
# of users report that it prevents them from uploading when it shouldn't.
#
#$PREF{urls_allowed_to_post_to_us_01}			= 'http://'  . $ENV{HTTP_HOST} . '/';
#$PREF{urls_allowed_to_post_to_us_02}			= 'https://' . $ENV{HTTP_HOST} . '/';



# PREFs Section 03: Security.
############################################################################
# FileChucker supports custom folder permissions, allowing you to specify 
# which user-levels (public, member, or admin) have read-only (RO) or
# read-write (RW) access (or no access) on a per-folder basis.  If you're
# also using UserBase, then you can create unlimited user-levels (i.e. 
# groups) and you can also specify permissions per individual user.
#
# If you don't specify any permissions for a given folder, then it inherits 
# the permissions from its parent folder; if no permissions have been set 
# for a folder or its parents, then the default rights specified here take
# effect.
#
# The $PREF{permissions_required_to_view_permissions} setting allows you to 
# control whether users can see what permission levels are set (only for
# folders that they can see).  Only admins can set/change permissions, 
# unless you are using UserBase and you have set the $PREF{enable_userdirs}
# setting, in which can you can allow users to adjust the permissions within
# their own userdir by setting the $PREF{users_can_change_perms_in_own_userdir}
# option.  By default this only allows the user to adjust whether the generic
# "public" and "members" groups have access to their folders, because in many
# cases you would not want your users to be able to see the other groups and
# usernames in your system.  But you can adjust this behavior as well using the
# users_changing_userdir_perms_can_see_other_groups/users settings.
#
# The $PREF{user_perms_override_group_perms_for_same_folder} setting (which 
# only applies when using UserBase, since without UserBase there are no
# individual users, only groups aka user-levels) specifies whether user or
# group permissions have higher priority when both are set for the same 
# folder.  When both are set but at different levels, the perms closest to 
# the folder in question are the ones that take effect.  For example, given
# folders foo, bar, and baz with these permissions set:
#
#	foo		-> set to RO for user "bob"
#	|--bar		-> set to RW for group "sales" (where bob is a member)
#	   |--baz	-> no perms set
#
# The effective permissions for bob are RO for foo, RW for bar, and RW for
# baz.
#
# Note that this feature requires a database, which you must configure
# in PREFs Section 12, and your database user must have these MySQL 
# privileges: Select, Insert, Update, Delete, Create.  Or if you want to
# manually create the table yourself, then the user does not need the Create
# privilege.
#
$PREF{enable_custom_folder_permissions}			= 'no';
$PREF{perms_table}					= 'folderperms';
$PREF{default_folder_rights}				= 'none'; # none, ro, rw; admins always have rw.
$PREF{permissions_required_to_view_permissions}		= 'rw';	  # none, ro, rw, or admin.
$PREF{user_perms_override_group_perms_for_same_folder}	= 'yes';  # requires UserBase.
$PREF{users_can_change_perms_in_own_userdir}		= 'yes';  # requires UserBase & $PREF{enable_userdirs}.
$PREF{users_changing_userdir_perms_can_see_other_groups}= 'no';
$PREF{users_changing_userdir_perms_can_see_other_users}	= 'no';



# PREFs Section 03: Security.
############################################################################
# Directory permissions: these should usually be 0777; on some servers, you
# may be able to get away with using less-permissive settings like 0755 or
# even 0700 instead.
#
# File permissions: these should usually be 0666; on some servers, you
# may be able to get away with using less-permissive settings like 0644 or
# even 0600 instead.
#
$PREF{writable_dir_perms}				= 0777;		# no quotes. default is 0777.
$PREF{writable_file_perms}				= 0666;		# no quotes. default is 0666.



# PREFs Section 03: Security.
############################################################################
# You can use a blacklist or a whitelist to prevent users from accessing the
# app.  A blacklist means "block this user" and a whitelist means "block
# EVERY user except this one", so in most cases you should use a blacklist
# instead of a whitelist.  If you specify both, then only the whitelist will
# be used, since it's the more restrictive of the two.
#
# These values are regular expressions, which means that some characters
# have special meanings (like dots) so they must be "escaped" using a back-
# slash, and that partial matching will be done unless you use "^" and "$"
# to mark the start and end of the value.  For example, if you want to match
# only the exact IP address 12.34.56.78, you would use the following:
#
#	$PREF{blacklisted_ip_addresses}{'01'} = '^12\.34\.56\.78$';
#
# Or if you want to match any IP that starts with 12.34., you'd use this:
#
#	$PREF{blacklisted_ip_addresses}{'01'} = '^12\.34\.';
#
# Or to match any IP that contains .34.56., you'd use this:
#
#	$PREF{blacklisted_ip_addresses}{'01'} = '\.34\.56\.';
#
# Note that the values here must be in single-quotes, not double-quotes.
#
# You can add as many rules as you want; just increment the number in '01',
# '02', etc.
#
$PREF{blacklisted_ip_addresses}{'01'}			= '';
$PREF{blacklisted_ip_addresses}{'02'}			= '';
$PREF{blacklisted_hostnames}{'01'}			= '';
$PREF{blacklisted_hostnames}{'02'}			= '';
#
$PREF{whitelisted_ip_addresses}{'01'}			= '';
$PREF{whitelisted_ip_addresses}{'02'}			= '';
$PREF{whitelisted_hostnames}{'01'}			= '';
$PREF{whitelisted_hostnames}{'02'}			= '';
#
$TEXT{failed_black_or_white_list}			= qq`Access denied based on blacklisted or whitelisted IP address or hostname.`;









# PREFs Section 04: User-directories.
############################################################################
# Only allow each user to access their own upload directory.  The user's
# directory is determined by the preferences you set below; it will either
# come from ?userdir=foo on the URL, or from a username cookie that's set
# by your site's existing login framework.  If you don't want any kind of
# username-based directories, and you want all users to be able to upload
# to wherever they want, then don't set this.  Finally note that even when
# this is set, administrators can still upload to and view any folder.
#
$PREF{enable_userdirs}					= 'no';
$PREF{userdir_folder_name}				= 'users';
$PREF{error_if_userdir_not_supplied}			= 'no';



# PREFs Section 04: User-directories.
############################################################################
# If you're dropping FileChucker into an existing system with lots of
# users, you may not want to manually create a user subdirectory for each
# one.  In that case you can enable this, and then anyone who visits with
# ?userdir=foo or with foo in their username cookie will cause the username
# directory to be created automatically.
#
$PREF{auto_create_userdirs}				= 'yes';



# PREFs Section 04: User-directories.
############################################################################
# Enable ?userdir=username (or ?userdir=whatever) on the URL to automatically
# select the upload subdirectory.  If you don't care about security, then you
# can also set $PREF{allow_userdir_on_url_insecurely} and be done with it.
# Yes, that's a bad idea, but people request this feature so there it is.
#
# But if you want to pass the userdir on the URL securely, then you must set
# $PREF{userdir_shared_secret} to a decently long string (30+ characters
# would be good) which will function sort of like a password.  Then in the
# (presumably PHP) page which is calling filechucker.cgi and is passing the
# userdir on the URL, you must do the following:
#
#	$userdir = 'whatever';
#	$secret = 'some longish and randomish string here';
#	$userdirhash = sha1($userdir . $secret); # http://php.net/sha1  if you're curious.
#
# Then when calling filechucker.cgi, however you're calling it, you must pass
# the following on the URL:
#
#	?...&userdir=$userdir&userdirhash=$userdirhash
#
# This way FileChucker can perform the same sha1() function and check its
# result against the userdirhash that was also passed, to verify that no
# one changed the userdir on the URL in an attempt to access a userdir that
# he shouldn't have access to.
#
$PREF{enable_userdir_on_url}				= 'no';
$PREF{allow_userdir_on_url_insecurely}			= 'no';
$PREF{userdir_shared_secret}				= '';



# PREFs Section 04: User-directories.
############################################################################
# If you're using enable_userdir_on_url, then you probably also want to set
# this keep_userdir_on_url option, so that when a user clicks on the various
# links like "Show Uploads," it keeps them inside their proper folder.
#
$PREF{keep_userdir_on_url}				= 'no';



# PREFs Section 04: User-directories.
############################################################################
# If you want per-username upload subdirectories, and you already have some
# kind of login framework in place on your site that stores usernames in
# cookies, then you can use this to automatically choose the right subdir
# based on the value in the cookie.  This means that each user will only
# be able to view and upload to his own subdirectory within your
# uploaded_files_dir.
#
$PREF{enable_userdir_from_cookie}			= 'no';
$PREF{userdir_cookie_name}				= 'username';



# PREFs Section 04: User-directories.
############################################################################
# If you are already storing a username/userdir variable in PHP sessions on
# your server, you can make FileChucker use that.
#
# For Method 1, you'll need to be calling FileChucker from the /upload/index.php
# file like this:
#
#	<?php
#		# set an environment variable from your PHP username variable:
#		session_start(); putenv("PHP_ENC_USERDIR=$username");
#		require("call_fc.php");
#	?>
#
# For Method 2, you don't necessarily need to call FileChucker exactly that
# way; instead, you'll need to have the PHP::Session Perl module installed on
# your server, and PHP's save_path will need to be readable from Perl.
#
$PREF{enable_userdir_from_php_session__method1}		= 'no';
$PREF{php_session_cookie_name}				= 'PHPSESSID';
$PREF{php_session_cache_ttl}				= 60*60*24; # in seconds.
#
$PREF{enable_userdir_from_php_session__method2}		= 'no';
$PREF{php_session_cookie_name}				= 'PHPSESSID';
$PREF{php_session_save_path}				= '/var/lib/php/session'; # or perhaps '/tmp';
$PREF{php_session_username_variable}			= 'username';



# PREFs Section 04: User-directories.
############################################################################
# If you have a set of default files/folders that you'd like to appear in
# each user's private directory, you can set this pref to the full path
# to the folder containing that default set.  The contents of this folder
# will be copied into each userdir the first time that user logs in.
#
$PREF{populate_each_new_userdir_from_this_folder}	= '';









# PREFs Section 05: Subdirectories.
############################################################################
# Allow users to upload to subdirectories if they want.
#
$PREF{enable_subdirs}					= 'yes';



# PREFs Section 05: Subdirectories.
############################################################################
# Allow users to create new subdirectories (but only within your
# uploaded_files_dir, of course).  You can also choose to only
# display a single "New subdir" textbox, even when the user is
# uploading multiple files, so that all the files in that one
# upload session will go into the same new subdirectory.  And if
# you want your users to be able to include multiple levels in
# the names of their new subdirs (i.e. create nested subdirs all
# at once) then set allow_multiple_levels_in_new_subdirs to 'yes'.
#
$PREF{only_allow_one_subdir_dropdown_per_upload}	= 'yes';
$PREF{enable_manual_creation_of_new_subdirs_during_upload}= 'yes';
$PREF{only_allow_one_new_subdir_per_upload}		= 'yes';
$PREF{max_num_of_subdir_levels}				= 5;
$PREF{max_length_of_new_subdir_names}			= 25;
$PREF{allow_multiple_levels_in_new_subdirs}		= 'no';



# PREFs Section 05: Subdirectories.
############################################################################
# FileChucker can automatically create a new subdirectory for each upload,
# and you can specify the name of this new subdirectory here.  It can
# include values from the user's cookies, from the URL, from any extra
# formfields that you have configured (see PREFs Section 07), and from the
# current date/time.
#
# Note that you must also set the enable_subdirs option (above), and also
# allow_multiple_levels_in_new_subdirs if you're specifying multiple levels
# here.
#
# To include variables from either the URL or from a cookie, use the format
# %URL{varname} or %COOKIE{cookiename}.  To use values that the user types
# into your form fields, use the format %FIELD{shortname}.  For example if
# you have $PREF{formfield_01_shortname} = 'company', then you can use 
# %FIELD{company}.  And you can include the value of any PREF by using
# %PREF{pref_name}.
#
# You can also use variables of the form %DATE{%v} to insert date/time values
# based on the standard date formatting variables; search the internet for the
# terms "unix man pages: date (1)" (or just run "man date" on any Unix system)
# for more information on the date format.
#
# If you're using an upload counter number (see $PREF{enable_upload_counter_number}
# in PREFs Section 09) you can include its value in your automatic new subdir
# name by using the variable #C.
#
# Anything not preceded by a percent-sign or a pound-sign will be passed 
# straight through as literal text.
#
# For example, if you set:
#
#	$PREF{automatic_new_subdir_name} = 'Job-%DATE{%Y%m%d}-%COOKIE{company}';
#
# ...and the user has a cookie called "company" set to "MyCo", and the date is
# say Feb 28 2006, then the new subdir will be named:
#
#	Job-20060228-MyCo
#
# Finally note that to disable this, you must comment it out or set
# it to null ('').
#
$PREF{automatic_new_subdir_name}			= '';



# PREFs Section 05: Subdirectories.
############################################################################
# When a new folder is created during an upload, either by the user choosing
# to create a new one on the upload form, or by automatic_new_subdir_name,
# we'll serialize it (add _01 to the end of its name) if a folder by that
# name already exists, unless you disable this.
#
$PREF{serialize_new_folders}				= 'yes';



# PREFs Section 05: Subdirectories.
############################################################################
# If you want to enable subdirectories, but do not want your users to be
# able to see the list of subdirectories on the upload form, then you can
# disable this.
#
# Whether or not this drop-down is displayed, you can pass ?path=/some/subdir/
# on the URL to specify the destination directory for the uploaded files.
# If the drop-down is displayed, then this has the effect of selecting the
# specified path by default, but the user can still change it.  If the drop-
# down is not displayed, then the path specified on the URL will be forced.
# Note that the $PREF{hide_path_to_uploads_dir} setting (PREFs Section 03)
# affects this option; if that setting is enabled, then the path specified on
# the URL must not include $PREF{uploaded_files_dir} on the front.  And
# conversely, if $PREF{hide_path_to_uploads_dir} is disabled, then the path
# specified on the URL *must* include $PREF{uploaded_files_dir} on the front.
#
$PREF{display_dropdown_box_for_subdir_selection}	= 'yes';
$PREF{hide_subdir_dropdown_when_passed_on_url}		= 'yes';



# PREFs Section 05: Subdirectories.
############################################################################
# A relatively frequent request is for the ability to allow uploads to
# subdirectories of your $PREF{uploaded_files_dir} folder, but not to
# that folder itself.  This option enables that behavior.
#
$PREF{force_all_uploads_into_subdirectories}		= 'no';









# PREFs Section 06: Email Notification.
############################################################################
# You can have the script send you an email whenever a new upload happens.
# It can be sent to as many recipients as you want.  Most of the email PREFs
# are fairly self-explanatory, but here are a few notes: the sender address
# doesn't have to be a real address, but it DOES have to end with a real
# domain name.  The smtp server is probably localhost or mail.yoursite.com,
# and we'll try both smtp and sendmail when trying to send an email. The
# email type can be either html or text, and the failure action can be
# either die_on_email_error or null, in which case we'll just ignore the
# error.  Note that if you set it to die_on_email_error, then that means
# we can't fork the sending operation off into a separate process, since we
# have to wait to make sure it completes; this means that the upload takes
# longer from the user's perspective (if the upload was big and the email-
# sending operation takes a while).  So once you've got FileChucker tested
# and are satisfied that the email portion works, you may want to NOT
# die on email error.
#
# SMTP Authentication is only needed if your mail server requires it.  If
# so, you'll need to set $PREF{path_to_sendmail} = ''.
#
# Note that if you want your users to be able to enter their own email
# address(es) on the upload form, to receive email notifications at those
# addresses, then you must configure a formfield for that, in PREFs Section 07.
#
# If you do enable an email-address formfield, you can choose to have the
# From: address on your notification emails be set to whatever address
# the user enters.  To do that, set the $PREF{sender_email_address_*}
# option(s) here to 'user_email_address'.
#
$PREF{email_notifications_to_webmaster}			= 'no'; # For the _1, _2, etc, settings below.
$PREF{email_notifications_to_userEntered_addresses}	= 'no';
$PREF{email_notifications_to_userbase_loggedin_address}	= 'no';
$PREF{email_notifications_to_userbase_folder_owner}	= 'no';
$PREF{attach_uploaded_files_on_webmaster_emails}	= 'no';
$PREF{attach_uploaded_files_on_user_emails}		= 'no';

$PREF{email_notification_recipient_1}			= 'me@example.com';
$PREF{sender_email_address_for_emails_to_webmaster}	= 'filechucker@example.com';
$PREF{sender_email_address_for_emails_to_users}		= 'filechucker@example.com';
$PREF{smtp_server}					= 'localhost:25'; # port is usually 25 or 587.
$PREF{smtp_auth_username}				= '';
$PREF{smtp_auth_password}				= '';
$PREF{path_to_sendmail}					= '/usr/sbin/sendmail';
$PREF{path_to_blat}					= 'c:\perl\bin\blat.exe'; # experimental.
$PREF{email_type}					= 'html';
$PREF{email_failure_action}				= 'die_on_email_error'; 



# PREFs Section 06: Email Notification.
############################################################################
# FileChucker can send a notification email to a specific address depending
# on the name of the folder into which the file was uploaded.  Note that the
# 'folder' values here must start with a slash, and a value of just '/' means
# the top-level of your uploads area (i.e. not in a subfolder).  The value
# for 'recipients' can include multiple addresses separated by commas.
#
#$PREF{email_notifications_per_folder}{'01'}{folder}		= '/sales';
#$PREF{email_notifications_per_folder}{'01'}{recipients}	= 'sales@example.com';
#$PREF{email_notifications_per_folder}{'02'}{folder}		= '/support';
#$PREF{email_notifications_per_folder}{'02'}{recipients}	= 'help@example.com';



# PREFs Section 06: Email Notification.
############################################################################
# Here you can set the subject and contents of the notification emails.  The
# notifications that go to the site webmaster(s) are separate from the ones
# that go to the user-entered email address(es), if any.
#
# The list of allowable variables includes all your formfield _shortname values
# (see PREFs Section 07), plus these built-in variables:
# 
# 	uploader_ipaddress 	uploader_hostname
# 	totalsize_bytes 	totalsize_nice
# 	userdir		 	username
# 	startetime	 	starttime_nice
# 	endetime	 	endtime_nice
# 	finalpath_local		filelist
#	counternum		serial_is_userdir_info
#
# If you do have some form fields enabled in PREFs Section 07, and you would 
# rather just have them all automatically included instead of specifying each
# one individually, then you can use the %%formfields%% and _formfields_template
# variables.  This is enabled by default.
#
# If you have FileChucker integrated with UserBase, then the following
# UserBase variables are also available:
#
#	ub_var_username		ub_var_realname
#	ub_var_email		ub_var_customfieldname
#
# The etime (epoch-time) variables %%startetime%% and %%endetime%% can also be
# formatted into date variables in any format you'd like, by using this
# syntax: 
#
#	%%endetime--date--#Y-#m-#d, #I:#M #p%%
#
# Search the internet for "unix man pages: date" (or just run the command
# "man date" on any Unix system) for more information on the date format.
#
# You can also include the values of any URL or cookie variables that you
# have set, by putting %URL{varname} or %COOKIE{varname} into your template.
#
# The %%filelist%% variable is for the names of the files in this upload.
# Each filename in the list is formatted based on the template in the
# $PREF{webmaster_notification_email_filelist_template} option or the
# $PREF{user_notification_email_filelist_template} option, and these
# can include the variables filename, filesize, linktofile, realpath,
# urlpath, localpath, filenum, and filecount.  Also, if you've created
# any formfields that are set to be "perfile", then they must go into
# this _filelist_template, not the main email template.
#
# For example:
#
#	$PREF{webmaster_notification_email_filelist_template} = qq`File %%filenum%% of %%filecount%%:\n%%filename%% (%%filesize%%)\n%%linktofile%%\n\n`;
#
# Or, if you are using HTML-formatted emails:
#
#	$PREF{webmaster_notification_email_filelist_template} = qq`<p>File %%filenum%% of %%filecount%%:<br /><a href="%%linktofile%%">%%filename%%</a> (%%filesize%%)</p>\n`;
#
#####
##### Webmaster email template:
#####


$PREF{webmaster_notification_email_subject} = "New upload on $ENV{HTTP_HOST}";

$PREF{webmaster_notification_email_filelist_template} = qq`<p>File %%filenum%% of %%filecount%%:<br /><a href="%%linktofile%%">%%filename%%</a> (%%filesize%%)</p>\n`;

$PREF{webmaster_notification_email_formfields_template} = qq`<p><b>%%name%%:</b> %%value%%</p>\n`;

$PREF{webmaster_notification_email_template} = qq`
<h1>New File(s) Uploaded</h1>
%%filelist%%

%%%if-formfields%%%
<p><br /></p><hr />
<h1>Custom Form Fields:</h1>
%%formfields%%
%%%end-formfields%%%

<p><br /></p><hr />
<h2>Technical Info:</h2>
<p>Upload Started: %%starttime_nice%%</p>
<p>Upload Finished: %%endtime_nice%%</p>
<p>Uploader's IP Address: %%uploader_ipaddress%%</p>
<p>Uploader's Hostname: %%uploader_hostname%%</p>
<p>Uploader's User-Agent: $ENV{HTTP_USER_AGENT}</p>
<p>Uploader's User-Dir: %%userdir%%</p>
<p>Uploader's Username: %%username%%</p>
<p>Total Uploaded Data: %%totalsize_nice%%</p>

<p><br /></p><hr />
<p>This message sent by FileChucker at:</p>
<p><a href="$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}">$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}</a></p>
`;


#####
##### User email template:
#####


$PREF{user_notification_email_subject} = "Upload confirmation from $ENV{HTTP_HOST}";

$PREF{user_notification_email_filelist_template} = qq`<p>File %%filenum%% of %%filecount%%:<br /><a href="%%linktofile%%">%%filename%%</a> (%%filesize%%)</p>\n`;

$PREF{user_notification_email_formfields_template} = qq`<p><b>%%name%%:</b> %%value%%</p>\n`;

$PREF{user_notification_email_template} = qq`
<h1>Thanks for your upload!</h1>
<p>Sincerely,</p>
<p>$ENV{HTTP_HOST}</p>
<p><br /></p><hr />
<p>This message sent by FileChucker at:</p>
<p><a href="$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}">$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}</a></p>
`;









# PREFs Section 07: Upload Form Configuration.
############################################################################
# Title appearing at the top of the page.  This can be text, HTML, an image,
# etc.  You can also create per-theme titles, for example light_title,
# round_title, etc, to give each theme/style a different title.
#
$PREF{title}						= '<div id="title">FileChucker</div>';
$PREF{title_uploader}					= '%PREF{title}';
$PREF{title_popupstatus}				= '%PREF{title}';
$PREF{title_uploadcomplete}				= '%PREF{title}';
$PREF{title_filelist}					= '%PREF{title}';
$PREF{title_login}					= '%PREF{title}';
$PREF{title_error}					= '%PREF{title}';
$PREF{title_default}					= '%PREF{title}';
#
# Uncomment these if you've installed the images from the zip file and you
# want the nice logos:
#
#$PREF{title}						= qq'<div id="title"><img src="%PREF{path_to_filelist_images}fclogo03.png" alt="FileChucker" /></div>';
#$PREF{dark_title}					= qq'<div id="title"><img src="%PREF{path_to_filelist_images}fclogo02.png" alt="FileChucker" /></div>';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Intro: text appearing below the title, before the upload form.
# Outtro: text appearing at the bottom of the form, just before the "Begin
# Upload" button.
#
$PREF{intro}						= '';
$PREF{intro_uploader}					= qq`<div id="intro">Upload your files here.</div>`;
$PREF{intro_popupstatus}				= '';
$PREF{intro_uploadcomplete}				= '';
$PREF{intro_filelist}					= '';
$PREF{intro_login}					= '';
$PREF{intro_error}					= '';
$PREF{intro_default}					= '';
#
$PREF{outtro}						= '';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# You may wish to allow your users to submit the form without including
# any files (i.e. if you've enabled some other form fields for collecting
# text input, and files will just be optional).  In that case, enable the
# _without_files setting here.  Or if you want to totally disable the file 
# fields, then set $PREF{num_default_file_elements} = 0 in PREFs Section 08.
#
$PREF{allow_form_submissions_without_files}		= 'no';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Miscellaneous mostly-self-explanatory options:
#
$PREF{add_new_file_upload_fields_automatically}		= 'yes';
$PREF{show_add_another_file_link}			= 'no';
$PREF{label_for_file_selector}				= qq`File <span class="filei">%%i%%</span> of <span class="fileitotal">%%numitems%%</span>:`;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# If you're embedding FileChucker into an existing layout, then you probably
# don't want FC to print out full HTML tags.  So you can disable that here.
# In that case you must also put the following lines into the <head> section 
# of your website's header/template file:
#
#	<script type="text/javascript" src="/cgi-bin/filechucker.cgi?js"></script>
#	<link rel="stylesheet" type="text/css" media="all" href="/cgi-bin/filechucker.cgi?css" />
#
# Note that the CSS output may have conditional comments at the bottom that
# you'll need to copy directly into the <head> section of your site.
#
# If you are not going to use print_full_html_tags, then ideally you'll be
# calling FileChucker from a file like /upload/index.shtml that contains
# something pretty similar to this:
#
#	<!--#include virtual="/header.shtml" -->
#	<!--#include virtual="/cgi-bin/filechucker.cgi?$QUERY_STRING" -->
#	<!--#include virtual="/footer.shtml" -->
#
# ...where header.shtml and footer.shtml contain your site-wide standard
# HTML code that each page is wrapped in.  Or, if your header/footer are
# in PHP, then your /upload/index.php might look like this:
#
#	<? virtual("/header.php"); ?>
#	<? virtual("/cgi-bin/filechucker.cgi?" . $_SERVER['QUERY_STRING']); ?>
#	<? virtual("/footer.php"); ?>
#
# However, if you are on a brain-dead server (for example, IIS6+) which
# does not support any decent way to call a CGI script that includes the
# proper server environment variables, and your server does not have PHP
# installed, and you still want to include a standard header/footer with
# FileChucker, then you can set encodable_app_template_file.  Set this to
# the full path (probably starting with "%PREF{DOCROOT}/") to an HTML page
# on your site which should be used as the template for FileChucker's
# output.  You can create this HTML file in whatever way you normally
# create web pages; the only requirements are that it contain the string
# %%encodable_app_output%% wherever you'd like FileChucker's output to
# appear, and that you put the strings %%css%% and %%js%% within the
# <head> section of the file.  No server-side processing (PHP, SSI, etc)
# will be done on the contents of this file; however you can specify a 
# title within it by inserting the string %%title%% (for example, as in
# <title>%%title%%</title>) and we'll replace that with your value for
# the title_for_template_file variable (or in some cases, with an
# internally-set title).
#
# UPDATE: as of 2012-04-16 (FileChucker trial 4.56t-e07), $PREF{print_full_html_tags}
# should no longer be disabled for embedding in most cases; instead, just
# include ?encembed=yes when embedding filechucker.cgi, as explained in the
# FAQ.
#
$PREF{print_full_html_tags}				= 'yes'; # overridable by the more specific ones next.
$PREF{print_full_html_tags_for_uploader}		= '';
$PREF{print_full_html_tags_for_popupstatus}		= 'yes'; # this one must be "yes" in most cases.
$PREF{print_full_html_tags_for_uploadcomplete}		= '';
$PREF{print_full_html_tags_for_filelist}		= '';
$PREF{print_full_html_tags_for_default}			= '';
$PREF{encodable_app_template_file}			= '';
$PREF{title_for_template_file}				= '';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Web servers treat "www.you.com" and "you.com" as two different domains,
# which matters for web applications that use cookies.  So you should make
# your website either always use the www, or always remove it.  You should
# be able to do this in your server configuration, but if not, you can do
# it here.  Whether to use www or not is only a matter of taste, so just 
# pick whichever way you want, and then stick with it.
#
$PREF{add_www_to_hostname}				= 'no';
$PREF{remove_www_from_hostname}				= 'no';
$PREF{prevent_direct_cgi_access}			= 'no';
$PREF{direct_cgi_access_error}				= qq`Direct CGI access is not allowed; <a href="%PREF{here}">go here instead</a>.`;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# You probably don't want to change these.
#
# Note that the 4 <div>s for perpage_container enable the rounded corners of
# the "round" theme.
#
$PREF{outer_container}					= '<div id="fcbody" class="%%on_page%%body">';
$PREF{perpage_container}				= '<div id="%%on_page%%page"><div id="fcc1"><div id="fcc2"><div id="fcc3"><div id="fcc4">';
$PREF{inner_container}					= '<div id="fc-container">'; # don't change the id here.
$PREF{page_content_wrapper_start}			= '<div id="fc_content">'; # don't change the id here.

$PREF{page_content_wrapper_end}				= '</div>';
$PREF{inner_container_end}				= '</div>';
$PREF{perpage_container_end}				= '</div></div></div></div></div>';
$PREF{outer_container_end}				= '</div>';

$PREF{print_filefields_wrapper_div}			= 'yes';
$PREF{print_file_element_wrapper_div}			= 'yes';

$PREF{viewpath_markup_start}				= '<div id="viewpath"><div id="viewpath-outer"><div id="viewpath-inner">';
$PREF{viewpath_markup_end}				= '</div></div></div>';

$PREF{footer_markup_start}				= '<div id="fcfooter"><div id="fcfooter-inner"><div id="fcfooter-text">';
$PREF{footer_markup_end}				= '</div></div></div>';

$PREF{title_inside_perpage_container}			= 'yes';
$PREF{footer_inside_perpage_container}			= 'yes';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Specify any custom text or HTML code to appear at the top or bottom of
# the pages.
#
$PREF{customcode_top}					= qq``;
$PREF{customcode_top_uploader}				= $PREF{customcode_top};
$PREF{customcode_top_popupstatus}			= $PREF{customcode_top};
$PREF{customcode_top_uploadcomplete}			= $PREF{customcode_top};
$PREF{customcode_top_filelist}				= $PREF{customcode_top};
$PREF{customcode_top_login}				= $PREF{customcode_top};
$PREF{customcode_top_error}				= $PREF{customcode_top};
$PREF{customcode_top_default}				= $PREF{customcode_top};
#
$PREF{customcode_bottom}				= qq``;
$PREF{customcode_bottom_uploader}			= $PREF{customcode_bottom};
$PREF{customcode_bottom_popupstatus}			= $PREF{customcode_bottom};
$PREF{customcode_bottom_uploadcomplete}			= $PREF{customcode_bottom};
$PREF{customcode_bottom_filelist}			= $PREF{customcode_bottom};
$PREF{customcode_bottom_login}				= $PREF{customcode_bottom};
$PREF{customcode_bottom_error}				= $PREF{customcode_bottom};
$PREF{customcode_bottom_default}			= $PREF{customcode_bottom};



# PREFs Section 07: Upload Form Configuration.
############################################################################
# You can adjust the text and the target for some of the footer links.
#
$PREF{home_link_name}					= "Home";
$PREF{home_link_url}					= "/";
$PREF{upload_files_link_label}				= "Upload";
$PREF{show_uploads_link_text}				= 'Download';
$PREF{administration_link_name}				= "Administration";



# PREFs Section 07: Upload Form Configuration.
############################################################################
# By default, we print certain footer links (like Home, Upload Files, Show
# Uploads, New Folder, etc) depending on which page we're on (the file-list
# shouldn't have a link to Show Uploads for example, because we're already
# on that page).  But if you want, you can override all our footer links by
# specifying your own.  Note that you can set $PREF{custom_footer} which is
# a shortcut to set all 4 of these to the same value.
#
# Alternatively, if you just want to add additional links to the current
# footer, then use $PREF{extra_footer_links}, like this:
#
#	$PREF{extra_footer_links} = [ '<a href="/foo">Foo</a>',  '<a href="/bar">Bar</a>' ];
#
#$PREF{custom_footer_for_uploader}			= '<div id="fcfooter"> </div>';
$PREF{custom_footer_for_popupstatus}			= '';
#$PREF{custom_footer_for_uploadcomplete}		= '<div id="fcfooter"> </div>';
#$PREF{custom_footer_for_default}			= '<div id="fcfooter"> </div>';
#$PREF{custom_footer_for_filelist}			= '<div id="fcfooter"> </div>';
#
$PREF{extra_footer_links} = [];



# PREFs Section 07: Upload Form Configuration.
############################################################################
# By default, if you upload a file that's 1 megabyte or bigger, the file 
# sizes and upload rate on the progress bar will be in MB and MB/s.  If you 
# want to force them to always be in KB instead, set these.
#
$PREF{force_KB_for_size_display}			= 'no';
$PREF{force_KB_for_transfer_rate_display}		= 'yes';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Specify the width of the progress bar, and whether to also display the
# progress table with it (containing times, sizes, etc).
#
$PREF{progress_bar_width}				= 350;
$PREF{show_progress_table_during_uploads}		= 'yes';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# You can choose to display the progress bar in a pop-up window if you wish.
#
$PREF{show_upload_status_in_popup_window}		= 'no';
$PREF{progress_bar_placeholder_message__popup}		= qq`Upload in progress; please wait.&nbsp; If this message appears for more than a few seconds, then your upload was probably very small and is already finished, so you can close this window.`;
$PREF{popup_status_uploading_message}			= qq`Upload in progress; please wait.<br />If progress bar does not appear,<br /><a href="#" onclick="this.href=document.getElementById(\\'juststatuslink\\').href; return true" target="_blank">click here</a> to display it.`;
$PREF{popup_status_window_javascript_code}		= qq`window.open(document.getElementById('juststatuslink').href,'fcstatuswindow','width=400,height=270,toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,copyhistory=no,resizable=yes');`;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# By default, when an upload begins, the progress bar pops out of nowhere
# and displays below the "Begin Upload" button.  If you want, you can set
# this preference so that it clears the rest of the page first, so that the
# progress bar & table are the only thing on the screen during the upload.
#
$PREF{clear_page_during_upload}				= 'yes';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# By default we'll use an iframe to do the upload, which means it happens
# without redirecting to another page upon completion.  This should be fine
# for any modern browser.  But if you do want to redirect to another page
# upon upload completion, you'll have to set $PREF{after_upload_redirect_to}
# in PREFs Section 10, which will automatically disable this setting.  Also
# note that disabling this setting will automatically enable the popup-
# based upload progress bar for Safari users, because otherwise the progress
# bar won't work in that browser.
#
$PREF{use_iframe_for_upload}				= 'yes';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# The placeholder message is displayed immediately after the "Begin Upload"
# button is clicked, before the progress bar is displayed.
#
# The "processing" message is displayed at the end of an upload, before we
# redirect to the "Upload Complete" page.
#
# Both of these can optionally contain HTML, images, etc.
#
$PREF{progress_bar_placeholder_message}			= qq`Upload in progress; please wait.&nbsp; Do not close this window.`;
$PREF{server_processing_upload_message}			= "Upload complete; the server is now processing your file(s).&nbsp; This could take a minute or two if your upload was very big.&nbsp; Please wait.";



# PREFs Section 07: Upload Form Configuration.
############################################################################
# To cancel an upload, the user only needs to click on some other link, or 
# click on one of their Favorites/Bookmarks, or type some other address into
# the browser's address bar, etc.  But some users feel more comfortable using
# an explicit "Cancel" link, so if you want to, you can enable such a link
# by setting this PREF.  For example:
#
#	$PREF{cancelbutton} = '<div><a href="/">Click here to cancel this upload.</a></div>';
#
$PREF{cancelbutton}					= '';



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Here you can specify your own custom Javascript code.  Leave off the
# <script> tags.  And you can use schedule_onload_action(myfunction); to
# hook into the onload logic.  If you want to specify code that should be
# executed just before the upload is submitted, put it into the __onsubmit
# code preference here.
#
$PREF{custom_js_code}					= qq``;
$PREF{custom_js_code__onsubmit}				= qq``;
$PREF{custom_js_code__onuploaddone}			= qq``;
$PREF{custom_js_code__uploadcomplete_page}		= qq``;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# You can specify your own HTML for custom form fields here.
#
# ! NOTE: in many cases this is overkill, and the built-in extra formfield
# ! options are a better choice.  Scroll down to the end of PREFs Section 07
# ! to use those options instead.
#
# The PREFs should contain your HTML code, for example:
#
#	$PREF{custom_form_fields_top___code}	= qq`Email Address:<input type="text" name="email" /> <br />Phone Number:<input type="text" name="phone" />`;
#
# The _top preference will be displayed on the upload form before the file
# fields, the _bottom will be displayed after the file fields, and the
# _perfile ones will be displayed once per file.  Or, if you want to specify
# your own file elements, you can do that, and in that case just stuff your
# entire custom form code into the _top___code PREF.
#
# For each custom form field in your code here, you must add the field's name
# to the $PREF{custom_form_fields_namelist} setting (comma-separated), so that
# FileChucker knows it should process that field.  Optionally, you can also
# create a $PREF{custom_form_fields_desclist} setting (comma-separated), to
# specify a slightly longer description for each field, which depending on your
# settings will be used in some contexts like notification emails and the file
# info page.  (Note: for any given form field, instead of adding it to the
# $PREF{custom_form_fields_namelist} setting, you can optionally create a
# $PREF{formfield_NN} setting [see end of PREFs Section 07], along with a
# $PREF{formfield_NN_custom}='yes' setting, in case you want to use any of the
# extra functionality provided by the other $PREF{formfield_NN_*} settings.)
#
# For any perfile code, the names of your perfile elements must end in _%i,
# for example:
#
#	$PREF{custom_form_fields_perfile___code}	= qq`File's author:<input type="text" name="author_%i" /> <br />File created at:<input type="text" name="location_%i" />`;
#
# If you want a given field to be mandatory, i.e. the form will not submit
# until the user enters a value, then add class="required" to the HTML code
# for the element.  For example:
#
#	$PREF{custom_form_fields_top___code}	= qq`Email Address:<input type="text" name="email" class="required" />`;
#
# You can also cause FileChucker to check that the value entered into an input
# element is a valid email address, by using class="emailformat" like this:
#
#	$PREF{custom_form_fields_top___code}	= qq`Email Address:<input type="text" name="email" class="required emailformat" />`;
#
# If you want to specify your own file elements as well (<input type="file" ... />)
# then you'll have to set $PREF{using_custom_file_elements} to 'yes'.  In
# this case you'll also need to specify the number of custom file elements.
# You MUST name your file elements exactly "uploadname1", "uploadname2", etc,
# and they must have "id" attributes set to those same values.
#
# If your code includes your own upload button, then you must set
# $PREF{upload_button} to null (below), and your button must include all of the
# following:
#
#	type="button" id="uploadbutton" class="default button" onclick="startupload()"
#
# For example:
#
#	<input type="button" value="Begin Upload" id="uploadbutton" class="default button" onclick="startupload()" />
#
# Or if you want to use type="image" instead of type="button" then you must
# change the onclick attribute to: onclick="startupload();return false".
#
$PREF{custom_form_fields_top___code}			= qq``;
$PREF{custom_form_fields_perfile___code}		= qq``;
$PREF{custom_form_fields_bottom___code}			= qq``;
$PREF{custom_form_fields_namelist}			= qq``;
$PREF{using_custom_file_elements}			= 'no';
$PREF{num_custom_file_elements}				= 5;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# This is the upload button.  If you want to use type="image" instead of
# type="button" then you must change the onclick attribute to:
# onclick="startupload();return false".
#
$PREF{upload_button}					= qq`<div id="uploadbuttonwrapper"><input type="button" value="Begin Upload" id="uploadbutton" class="default button" onclick="startupload()" /></div>`;



# PREFs Section 07: Upload Form Configuration.
############################################################################
# Extra formfields/textboxes (including email fields & drop-down lists):
#
# Allow the user to enter comments or information about the file(s) that
# they are uploading.  This information can be emailed to you as well as
# saved on the server in a text file and/or a database.
#
# You should specify a _shortname PREF for each form field; this may contain
# only letters, numbers, and underscores.  It is used for the "name" attribute
# of the form element, and for the name of the database column/field if you're
# storing your upload info in a database (see PREFs Section 09).  Note however
# that you can omit the _shortname PREF, in which case FileChucker will create
# a _shortname for the field based on the $PREF{formfield_NN} value.
#
#	$PREF{formfield_01}			= "Company Name:";
#	$PREF{formfield_01_shortname}		= "company"; # becomes the DB column name.
#
# The default form-field type is a single-line text box, but you can make
# a multiline box (i.e. a <textarea>) by adding the _multiline option:
#
#	$PREF{formfield_01}			= "Description:";
#	$PREF{formfield_01_multiline}		= 'yes';
#
# The default position is 'top', i.e. above the file input field(s)s, but you
# can specify 'bottom' or 'perfile' to position the formfield there instead:
#
#	$PREF{formfield_01}			= "Description:";
#	$PREF{formfield_01_position}		= 'bottom'; # or 'perfile'.
#
# If you want some additional text to be displayed on the upload form instead
# of just the name of the field, you can create a _displayname PREF:
#
#	$PREF{formfield_01}			= "Address:";
#	$PREF{formfield_01_displayname}		= "Address (be sure to include your zip code):";
#
# You can specify that FileChucker should save the user's input in a cookie,
# and then auto-fill the the textbox from that cookie the next time that 
# visitor loads the page, by setting a _save PREF like this:
#
#	$PREF{formfield_01}			= 'Company:';
#	$PREF{formfield_01_save}		= 'yes';
#
# You can create a _required PREF for any formfield, which will force the
# user to enter a value before allowing the form to be submitted.
#
#	$PREF{formfield_01}			= 'Company:';
#	$PREF{formfield_01_required}		= 'yes';
#
# To make a drop-down list, use the following example.  Note that the
# _dropdown_values PREF is optional; you should only use it if you want
# the values submitted to be different from the values displayed.
#
#	$PREF{formfield_01}			= 'Department:';
#	$PREF{formfield_01_email}		= 'yes';
#	$PREF{formfield_01_dropdown}		= '|||Sales|||Support|||Other';
#	$PREF{formfield_01_dropdown_values}	= '|||sales@example.com|||help@example.com|||contact@example.com';
#	$PREF{formfield_01_emailtemplate}	= 'webmaster'; # optional; probably desirable for this particular formfield.
#
# You can also create a drop-down list that's populated by an SQL query.  This
# of course requires that you set the database options in PREFs Section 12.
# Then set the formfield_NN_dropdown to the SQL query that returns the values
# you want to use.  Since drop-down lists can have separate values for the
# displayed text and the submitted text, you can use an SQL statement that
# returns either one or two columns.  For example, to use a single column
# for both the displayed and submitted values, use this:
#
#	$PREF{formfield_01_dropdown} = 'SELECT `emailaddr` FROM `tablename` WHERE [...]';
#
# Or, to use 2 columns, submitting a different value than the displayed value:
#
#	$PREF{formfield_01_dropdown} = 'SELECT `name`,`emailaddr` FROM `tablename` WHERE [...]';
#
# In either case, the portion of the query from SELECT to FROM must be exactly
# as shown here; you can of course adjust the column names, but the spacing,
# quotes, and capitalization of SELECT and FROM must remain unchanged.
#
# You can also make _radio and _checkbox elements; see the examples below.
#
# To pre-fill a form field with a default value, you can create a _default
# setting for it, which can include URL variables using the syntax %URL{varname},
# cookie variables using the syntax %COOKIE{cookiename}, pref values using the
# syntax %PREF{prefname}, and environment variables using the syntax %ENV{varname}.
# You can include the result of a MySQL select statement by using the syntax
# %SQL{{SELECT `foo` FROM `bar` WHERE ...}}.  Any custom UserBase fields can be
# accessed via %PREF{ub_var_varname}; for example a field named "city" would be
# %PREF{ub_var_city}.  Here's an example:
#
#	$PREF{formfield_01}			= 'Full Name:';
#	$PREF{formfield_01_default}		= '%COOKIE{full_name}';
#
# To make a hidden field, create a _hidden setting.  In this case you'll also
# need to specify a _default setting to give the field a value.
#
# You can specify a string value (text, HTML, etc) to appear before or
# after any given formfield by creating a _before or _after PREF for it:
#
#	$PREF{formfield_01}			= "Phone:";
#	$PREF{formfield_01_after}		= "<p>(Phone number will not be sold or redistributed.)</p>";
#
# You can automatically clean up any submitted text.  This will remove any
# characters except 0-9A-Za-z._- and will replace spaces with underscores:
#
#	$PREF{formfield_01}			= "Company Name:";
#	$PREF{formfield_01_clean}		= "yes";
#
# The _numeric option forces the user to only enter numbers:
#
#	$PREF{formfield_01}			= "PO Number:";
#	$PREF{formfield_01_numeric}		= "yes";
#
# To prevent a field from being processed at all when it's null (for example,
# an unchecked checkbox), you can set a _skip_if_null PREF for it:
#
# 	$PREF{formfield_01_skip_if_null}	= 'yes';
#
# If you have multiple checkbox fields and you'd like them all to get stored
# into a single field if they're checked -- as opposed to the default checkbox
# behavior which is for each one to be stored individually with a "yes" or "no"
# value -- then you can add a _group PREF for each such checkbox, and create a
# special formfield_groupname PREF for them:
#
#	$PREF{formfield_01}			= 'strawberry';
#	$PREF{formfield_01_checkbox}		= 'yes';
#	$PREF{formfield_01_group}		= 'flavors';
#
#	$PREF{formfield_02}			= 'blueberry';
#	$PREF{formfield_02_checkbox}		= 'yes';
#	$PREF{formfield_02_group}		= 'flavors';
#
#	$PREF{formfield_03}			= 'apple';
#	$PREF{formfield_03_checkbox}		= 'yes';
#	$PREF{formfield_03_group}		= 'flavors';
#
#	$PREF{formfield_flavors}		= 'Flavors:';
#	$PREF{formfield_flavors_shortname}	= 'flavors';
#	$PREF{formfield_flavors_is_group_master}= 'yes';
#	$PREF{formfield_flavors_group_separator}= ' || ';
#
# All checkbox values will be converted to "yes" or "no", unless the checkbox is
# part of a _group, or unless you create a _binary PREF for it, which will save
# it as a 1 or a 0, or a _raw PREF for it, which will use the browser's default,
# which is usually "on" or null.
#
# You can transform any submitted value to a different value by creating a
# _transform PREF for it.  For example, the following will change a submitted
# value of "tv" to "television":
#
#	$PREF{formfield_01_transform_tv}	= 'television';
#
# If you are enabling reprocessing on your site (see PREFs Section 09) then you
# can add a formfield PREF called _reprocessing and set it to "refill" to cause
# that textbox to be refilled with the value from the original upload, as long
# as you have the upload info stored in a database (PREFs Section 09).  This is
# in some ways similar to the _save option, but whereas that refills the textbox
# from a cookie on the user's computer, this refills it from the value in your 
# database.  You can also specify "readonly" in the same preference to cause the 
# refilled value to be unchangable by the user.  Specify "skip" or "hide" to 
# skip/hide this formfield during reprocessing. You can also specify 
# "fill_with_num_files_selected" (self-explanatory).
#
#	$PREF{formfield_01}			= "Company Name:";
#	$PREF{formfield_01_reprocessing}	= "refill,readonly";
#
# Finally,you can use any formfield as an email address field, to which a
# notification email can be sent, by creating an _email PREF:
#
#	$PREF{formfield_01}			= 'Email Address:';
#	$PREF{formfield_01_email}		= 'yes';
#
# Then the formfield will accept one or more email addresses separated by commas
# and/or spaces, and notification of the upload including a link to the file(s)
# can be sent to the specified address(es).  You must configure the email
# notification PREFs (see PREFs Section 06) for this to work.  Note that you 
# should probably only create such an email field if you are requiring your 
# users to be logged in before they can upload.  This is because if you allow 
# just anybody to enter an email address, and you then send an email to that 
# address, you have created an open invitation for spammers to abuse your 
# website.  They can hit it thousands of times per day and send their spam to
# as many addresses as they want.
#
# If you want the entered email address to receive an email based on the
# webmaster email template instead of the user email template (see PREFs 
# Section 06), then also set the following:
#
#	$PREF{formfield_01_emailtemplate}	= 'webmaster';
#
# The following examples are commented-out so they are inactive. You can 
# uncomment them (delete the leading "#") and edit them, or create your own.
#
# EXAMPLES:
#
#	$PREF{top_formfields_title}			= 'Please enter the following information:';
#	
#	$PREF{formfield_01}				= 'Company:';
#	$PREF{formfield_01_save}			= 'yes';
#	$PREF{formfield_01_required}			= 'yes';
#	$PREF{formfield_01_shortname}			= 'company';
#	
#	$PREF{formfield_02}				= 'Description of upload:';
#	$PREF{formfield_02_multiline}			= 'yes';
#	$PREF{formfield_02_shortname}			= 'description';
#	
#	$PREF{formfield_03}				= 'Email Address:';
#	$PREF{formfield_03_save}			= 'yes';
#	$PREF{formfield_03_email}			= 'yes';
#	$PREF{formfield_03_required}			= 'yes';
#	$PREF{formfield_03_shortname}			= 'email_address';
#	
#	$PREF{formfield_04}				= 'Gender:';
#	$PREF{formfield_04_dropdown}			= '|||M|||F|||Other';
#	$PREF{formfield_04_required}			= 'yes';
#	$PREF{formfield_04_shortname}			= 'gender';
#	
#	
#	
#	$PREF{perfile_formfields_title}			= 'About this file:';
#	
#	$PREF{formfield_05}				= 'Created by:';
#	$PREF{formfield_05_shortname}			= 'creator';
#	$PREF{formfield_05_position}			= 'perfile';
#	
#	$PREF{formfield_06}				= 'Creation date:';
#	$PREF{formfield_06_shortname}			= 'creation_date';
#	$PREF{formfield_06_position}			= 'perfile';
#	
#	
#	
#	$PREF{bottom_formfields_title}			= 'Additional comments (optional):';
#	
#	$PREF{formfield_07}				= '';
#	$PREF{formfield_07_multiline}			= 'yes';
#	$PREF{formfield_07_shortname}			= 'comments';
#	$PREF{formfield_07_position}			= 'bottom';
#	
#	$PREF{formfield_08}				= 'Choose an item:';
#	$PREF{formfield_08_radio}			= 'yes';
#	$PREF{formfield_08_option01_value}		= 'ITEM001';
#	$PREF{formfield_08_option01_label}		= 'Black and white print';
#	$PREF{formfield_08_option02_value}		= 'ITEM002';
#	$PREF{formfield_08_option02_label}		= 'Color print';
#	$PREF{formfield_08_option03_value}		= 'ITEM003';
#	$PREF{formfield_08_option03_label}		= 'T-shirt';
#	$PREF{formfield_08_default}			= 'ITEM001';
#	$PREF{formfield_08_item_separator}		= "<br /><br />";
#	$PREF{formfield_08_shortname}			= "product";
#	$PREF{formfield_08_position}			= 'bottom';
#	
#	$PREF{formfield_09}				= 'Would you like your items gift-wrapped?';
#	$PREF{formfield_09_checkbox}			= 'yes';
#	$PREF{formfield_09_default}			= '';
#	$PREF{formfield_09_shortname}			= "giftwrapping";
#	$PREF{formfield_09_position}			= 'bottom';









# PREFs Section 08: Upload Restrictions.
############################################################################
# Allow the user to upload multiple files at the same time, up
# to this limit.
#
$PREF{max_files_allowed}				= 5;
$PREF{num_default_file_elements}			= 1;



# PREFs Section 08: Upload Restrictions.
############################################################################
# Set the maximum amount of data that can be uploaded at once.  Note that
# this is per upload, not per file; if you set this to 10 megabytes, then
# you can upload one 10MB file, or two 5MB files, etc, as long as the sum
# is not more than your limit.  Note that one megabyte is 1024*1024*1; 
# 5 MB is 1024*1024*5, etc.
#
$PREF{sizelimit_for_strangers}				= 1024*1024*100;
$PREF{sizelimit_for_members}				= 1024*1024*500;
$PREF{sizelimit_for_admins}				= 1024*1024*2000;



# PREFs Section 08: Upload Restrictions.
############################################################################
# You can specify a quota for your upload directory.  You can also specify
# a quote for each userdir, if you have userdirs enabled (see PREFs Section
# 04).  Note that these values are in bytes; to specify them in megabytes,
# multiply by 1024*1024, for example 1024*1024*1 is one MB, 1024*1024*5 is
# five MB, etc.  Set them to zero to disable the quotas.
#
$PREF{quota_for_entire_upload_directory}		= 0;
$PREF{quota_for_member_userdirs}			= 0;



# PREFs Section 08: Upload Restrictions.
############################################################################
# You can allow or disallow uploads based on file extension.  Each of these
# preferences takes a list of extensions separated by spaces.  The period
# must be included with the extension.  For example:
#
#	$PREF{only_allow_these_file_extensions} 	= '.jpg .png .gif';
#
# Finally, note that these are not case sensitive.
#
$PREF{only_allow_these_file_extensions}			= '';
$PREF{disallow_these_file_extensions}			= '.exe .php .php3 .php4 .php5 .phtml .cgi .pl .sh .py .js .htaccess .htpasswd .cmd .bat';
$PREF{allow_files_without_extensions}			= 'yes';
$PREF{disallow_these_strings_within_filenames}		= '\.php \.asp \.cgi \.pl$ \.plx torrent dvdrip'; # can include regexes, so periods must be escaped.  must be in single quotes.
#
$TEXT{illegal_filename_message}				= qq`Filename or file type not allowed: %%filename%%`;



# PREFs Section 08: Upload Restrictions.
############################################################################
# In both filenames and directory names, convert spaces to underscores,
# and remove anything that's not in the set [0-9A-Za-z._-].
#
$PREF{clean_up_filenames}				= 'yes';









# PREFs Section 09: Processing Uploads.
############################################################################
# In PREFs Section 03: Security, there is a option "serialize_all_uploads"
# that adds a long (~40 digit) serial number to the end of all filenames.
# But even if that option is disabled, if you don't set the 
# overwrite_existing_files option here, then a serial number WILL be
# appended onto the filename if a file by the same name already exists.
# Alternatively, you can set the nice_serialization options here, which
# will add a number like "_01" or " 01" if a file by the same name already
# exists.  So in summary, you can have all files serialized (long number),
# all files nice-serialized (2-digit number), only serialize when filename
# already exists (either long or 2-digit serial), or overwrite existing files
# (i.e. never serialize).  Note that regular- and nice-serialization are
# mutually exclusive, and that regular (serialize_all_uploads) takes
# precedence if both are set, since it's a security feature.
#
$PREF{overwrite_existing_files}				= 'no';
$PREF{nice_serialization_when_file_exists}		= 'yes';
$PREF{nice_serialization_always}			= 'no';



# PREFs Section 09: Processing Uploads.
############################################################################
# You can have a datestamp (YYYYMMDD-HHMM) added to the filename for
# each upload.  It will be added to the end, right before the extension.
#
$PREF{datestamp_all_uploads}				= 'no';



# PREFs Section 09: Processing Uploads.
############################################################################
# FileChucker can operate in a few special upload modes:
#
# Replace mode lets users upload files that already exist on the server,
# overwriting those files.  If you have any extra formfields enabled,
# they will not be shown in replace mode -- it's only for replacing the
# files themselves.
# 
# Reprocessing mode lets users go through the upload process, filling out
# any extra formfields that you have enabled; but instead of uploading
# files, it uses files that have been uploaded before and are already on
# the server.
#
# AddFile mode lets users upload new files, but does not show any of your
# extra formfields.
#
# These are disabled by default because most people probably won't have a
# use for them.
#
$PREF{enable_replace_mode}				= 'no';
$PREF{enable_reprocessing_mode}				= 'no';
$PREF{enable_addfile_mode}				= 'no';
$PREF{label_for_replace_action}				= 'Replace';
$PREF{label_for_reprocess_action}			= 'Reprocess';
$PREF{label_for_addfile_action}				= 'Add New Files';
$PREF{reprocessing_mode_file_list_message}		= "Reprocessing: %%folder_name%% [%%num_files%% file(s)]";
$PREF{reprocessing_mode_file_list_done_message}		= "Reprocessed: %%folder_name%% [%%num_files%% file(s)].";
$PREF{list_filenames_on_reprocessing_form}		= "no";
$PREF{pass_filenames_when_reprocessing_is_done}		= "no";



# PREFs Section 09: Processing Uploads.
############################################################################
# You can give each upload a unique serial number, which can start at any
# value you wish, and which increases by 1 for each upload.  You can then
# use this number in your notification emails, etc.  This number will be
# stored on your server in the file $PREF{datadir}/_fc_counter_value.txt.
# To start your upload counter number at some specific value, just edit
# the number in that file.
#
$PREF{enable_upload_counter_number}			= 'no';
$PREF{pad_with_zeros_to_this_length}			= 5;



# PREFs Section 09: Processing Uploads.
############################################################################
# FileChucker can automatically rename every file that gets uploaded,
# based on a format that you specify here.
#
# You can use the following variables in your filename formatting:
#
#	#O - original filename from the user's computer (without extension)
#
#	#E - extension from original filename (without leading period)
#
#	#U - name of user's private directory (null unless you've 
#	     enabled the userdir PREFs)
#
#	#N - sequence number of this file within its original upload
#	     (set to 1 if only a single file was uploaded)
#
#	#C - upload counter number (see $PREF{enable_upload_counter_number}
#	     in PREFs Section 09)
#
# You can also use variables of the form %DATE{%v} to insert date/time
# values based on the standard date formatting variables; Google for
# "unix man pages: date (1)" (or just run "man date" on any Unix
# system) for more information on the date format.
#
# If you've enabled any extra formfields (PREFs Section 07), you can
# use the values from those fields in renaming the uploaded files.
# Just use the _shortname from the PREF within a %FIELD container.
# For example if you have $PREF{formfield_01_shortname} = 'company',
# then you can use %FIELD{company}.
#
# You can include variables from either the URL or from a cookie by using
# %URL{varname} or %COOKIE{cookiename}, and you can include the value of
# any preference by using %PREF{pref_name}.
#
# And anything not preceded by a pound-sign or a percent-sign will be 
# passed straight through as literal text.
#
# For example, if you set:
#
#	$PREF{reformat_filenames_for_all_uploads} = '%DATE{%Y%m%d}-#U_#N-%COOKIE{foo}-#O.#E';
#
# ...and then a user uploads 3 files, on say Feb 28 2006, then they
# will be renamed to:
#
#	20060228-userdirname_1-fooCookieValue-originalfilename.ext
#	20060228-userdirname_2-fooCookieValue-originalfilename.ext
#	20060228-userdirname_3-fooCookieValue-originalfilename.ext
#
# Finally note that to disable this, you must comment it out or set
# it to null ('').
#
$PREF{reformat_filenames_for_all_uploads}		= '';



# PREFs Section 09: Processing Uploads.
############################################################################
# This setting controls how uploads are processed internally.  It should
# probably be set to 'yes' in most cases.
#
$PREF{move_tmpfile_instead_of_copying_contents}		= 'yes';



# PREFs Section 09: Processing Uploads.
############################################################################
# FileChucker can run a virus-scan command on the uploaded files, assuming
# you have a command-line virus scanner on your server.
#
$PREF{scan_uploads_for_viruses}				= 'no';
$PREF{virus_scan_command}				= 'clamscan "%%filename%%"';



# PREFs Section 09: Processing Uploads.
############################################################################
# You can optionally copy the uploaded files to another server via FTP.
# This will happen automatically at the very end of the upload process.
# The base_path setting is the folder on the FTP server where you'd like
# the files transferred into, and the create_subdirs setting determines
# whether to recreate the directory structure that each file has on the
# server where FileChucker is installed (i.e. if the user chose to upload
# into a subfolder, or created a new subfolder, etc) -- if disabled, all
# files will be transferred into base_path with no subfolders created.
#
$PREF{ftp_files_to_another_server_after_upload}		= 'no';
$PREF{ftp_server}					= 'myothersite.com';
$PREF{ftp_username}					= 'myuser';
$PREF{ftp_password}					= 'mypass';
$PREF{use_passive_ftp_mode}				= 'no';
$PREF{extensions_to_use_ascii_mode_for}			= '\.txt \.htm \.html \.shtml'; # regexes.
$PREF{base_path_on_ftp_server}				= '/pub';
$PREF{create_subdirs_on_ftp_server}			= 'yes';
$PREF{delete_files_on_this_server_after_successful_ftp}	= 'no';



# PREFs Section 09: Processing Uploads.
############################################################################
# You can log information about each uploaded file, like the uploader's
# IP/hostname/user-agent, timestamps, elapsed time, etc.  This information
# will be logged in a database, and requires that you set the database
# preferences in PREFs Section 12.
#
# The following built-in data fields will be logged by default:
#
#	filepath,filename,origpath,origname,filesize,uploadsize,filecount,
#	serial,ip,host,userdir,username,useragent,starttime,endtime,
#	startetime,endetime,elapsecs,elapmins,elaphours,counternum
#
# Each row in the database represents one uploaded file,
# not one upload session.  Unless of course you've configured FileChucker
# to only allow one file to be uploaded at a time, in which case there IS
# only one uploaded file in one upload session.
#
# You can also log the values of URL variables, by setting the
# $PREF{store_values_from_these_url_variables} option. This should be a
# list separated by commas and/or spaces.
#
# You can use a $PREF{db_column_name_conversions} setting in case some of
# your database column names don't match our built-in variable names.  For
# example, if you want to store the filename into a field called "image" in
# your database, you'd need to do the following:
#
#	$PREF{db_column_name_conversions}{image} = 'filename';
#
$PREF{store_upload_info_in_database}			= 'no';
$PREF{upload_log_table}					= 'upload_info'; # will be created automatically.
$PREF{db_columns_for_upload_info}			= 'filepath,filename,origpath,origname,filesize,uploadsize,filecount,serial,ip,host,userdir,username,useragent,starttime,endtime,startetime,endetime,elapsecs,elapmins,elaphours,counternum';
$PREF{automatically_store_my_formfields_in_db}		= 'yes'; # requires $PREF{store_upload_info_in_database}.
$PREF{db_column_name_conversions}{foobar}		= '';
$PREF{store_values_from_these_url_variables}		= ''; # You must add these to db_columns_for_upload_info too.



# PREFs Section 09: Processing Uploads.
############################################################################
# In addition to the $PREF{store_upload_info_in_database} setting above, you
# can also specify individual SQL statements to be executed.  This requires
# that you set the database preferences in PREFs Section 12, but it doesn't
# use any other settings.  In these statements, you can use any of the
# built-in field names specified in the $PREF{store_upload_info_in_database} 
# documentation above, as well as any of your custom form fields via their
# _shortname identifiers.  To use the values of any of those fields in your
# statement, use the syntax %FIELD{fieldname}.  For example:
#
#	$PREF{custom_sql_command}{'01'} = "INSERT INTO `sometable` (`filename`) VALUES('%FIELD{filename}')";
#
# You can also use %URL{varname} and %COOKIE{cookiename} to insert values
# from the URL's query-string and from any cookies you may have.  And you
# can use %PREF{prefname} if you want to insert the values of any prefs.
#
# Currently, INSERT is the only supported SQL function here.
#
$PREF{enable_custom_sql_commands}			= "no";
$PREF{custom_sql_command}{'01'}				= "";
$PREF{custom_sql_command}{'02'}				= "";









# PREFs Section 10: Post-Upload.
############################################################################
# After a successful upload, we normally display a page that says "upload 
# complete" and lists the uploaded files, their sizes, etc.  If you want,
# you can redirect to some other page instead.  Note that you can include
# variables in the value from the URL, from a cookie, from any of your 
# formfields, or from any PREF value by using %URL{varname},
# %COOKIE{cookiename}, %FIELD{shortname}, or %PREF{prefname}
# in the redirect value.  For example:
#
#	$PREF{after_upload_redirect_to} = 'http://example.com/foo/bar/?baz=%URL{baz}&bim=%COOKIE{bim}&bop=%FIELD{bop}';
#
# You can also include the %%foldername%% variable, which will be replaced
# by the name of the subfolder that the (first) uploaded file went into.
#
# If you're using an upload counter number (see $PREF{enable_upload_counter_number}
# in PREFs Section 09) you can include its value in the URL by using the
# variable %%counternum%%.
#
# All the relevant information will be passed on the query-string to your
# redirection URL, including any error-state information.
#
$PREF{after_upload_redirect_to}				= '';
$PREF{pass_original_querystring_through}		= 'yes';
$PREF{pass_default_data_on_redirect}			= 'yes';
$PREF{pass_filenames_on_redirect}			= 'yes';
$PREF{pass_formfield_values_on_redirect}		= 'yes';



# PREFs Section 10: Post-Upload.
############################################################################
# Templates for the upload-complete page.  For both of these, you can also
# create a second version ending in ___reprocessing, if you're using the
# reprocessing feature and want it to have a different upload-complete page.
# If you want to display the values from any extra formfields that you've
# added to your upload form, add %FIELD{fieldname} to your template below,
# where "fieldname" is the _shortname for the field in question.
#
$PREF{upload_complete_page_template}			= qq`
<dl id="fcuploadsummary">
<dt class="first">Your upload is complete:</dt>
<dd>Elapsed time %%elapsed_time%%</dd>
<dd>Total upload size %%total_upload_size%%</dd>
<dd>Average speed %%average_speed%%</dd>
	%%%if-formfields%%%
	<dt>Your information:</dt>
	%%formfields%%
	%%%end-formfields%%%
%%filelist%%
<dt>Another Upload?</dt>
<dd><a href="%PREF{here_uploader}%PREF{default_url_vars}">Return to upload page</a>.</dd>
</dl>
`;
#
$PREF{upload_complete_filelist_template}		= qq`
<dt>File %%filenum%% of %%total_file_count%%:
%%%if-illegal%%% skipped because the filetype is not allowed.</dt> %%%end-illegal%%%
%%%if-replaceerror%%% skipped because we are in Replace Mode and that file does not exist on the server.</dt> %%%end-replaceerror%%%
%%%if-viruserror%%% skipped because the file failed the virus scan.</dt> %%%end-viruserror%%%
%%%if-success%%%
<a href="%%link%%">%%filename%%</a></dt>
<dd>%%filesize%% uploaded successfully.</dd>
<dd>URL to file:  <input name="urltoupload%%filenum%%" id="urltoupload%%filenum%%" value="%%link_with_fqdn%%" onclick="this.select();" type="text"></dd>
<dd>HTML code:  <input name="htmlforupload%%filenum%%" id="htmlforupload%%filenum%%" value="&lt;a href=&quot;%%link_with_fqdn%%&quot;&gt;%%filename%%&lt;/a&gt;" onclick="this.select();" type="text"></dd>
<dd>BBCode:  <input name="bbcodeforupload%%filenum%%" id="bbcodeforupload%%filenum%%" value="[URL=%%link_with_fqdn%%]%%filename%%[/URL]" onclick="this.select();" type="text"></dd>
%%%if-isimage%%%<dd>Img:  <input name="imgcodeforupload%%filenum%%" id="imgcodeforupload%%filenum%%" value="[img]%%link_with_fqdn%%[/img]" onclick="this.select();" type="text"></dd>%%%end-isimage%%%
	%%%if-perfile_formfields%%%
	<dt>File information:</dt>
	%%perfile_formfields%%
	%%%end-perfile_formfields%%%
%%%end-success%%%
`;









# PREFs Section 11: File-List Configuration.
############################################################################
# Options for controlling the display of the uploaded-files list.
# You can set the unit, number of decimal places, and the color
# that the rows turn to when you hover the mouse over them.  You
# can also specify how the date should be displayed.  Google for
# "unix man pages: date (1)" (or just run "man date" on any Unix
# system) for more information on the date format.
#
$PREF{unit_for_size_display_in_uploaded_files_list}	= 'KB'; # must be 'KB', 'MB', or 'mixed'.  See PREFs Section Z if you want Ko/Mo.
$PREF{num_decimals_for_uploaded_files_list_sizes}	= 0;
$PREF{shortened_display_filename_length___listmode}	= 35; # characters.
$PREF{shortened_display_filename_length___gridmode}	= 20; # characters.
$PREF{date_format_for_filelist}				= '%b%d, %I:%M%P';
#$PREF{date_format_for_filelist}			= '%Y-%m-%d, %I:%M %P';
#$PREF{date_format_for_filelist}			= '%a %b %d, %Y, %H:%M';
#$PREF{date_format_for_filelist}			= '%I:%M %P %b %d %Y';
$PREF{only_show_files_with_these_extensions}		= '';
$PREF{hide_files_with_these_extensions}			= '.exe .php .php3 .php4 .php5 .phtml .cgi .pl .sh .py .htaccess .htpasswd .DS_Store';
$PREF{hide_items_whose_names_match}			= 'fcimages fcht fcziptmp _vti_cnf \.DS_Store'; # can include regexes, so periods must be escaped.  must be in single-quotes.
$PREF{time_offset}					= -0; # in hours; can include negative sign.



# PREFs Section 11: File-List Configuration.
############################################################################
# The file list can be displayed as a detailed list, or as a grid (useful
# when most of your files are images and you have thumbnails enabled).
# You can also choose to disable altogether the menu controlling these
# options.
#
$PREF{enable_multiple_filelist_modes}			= 'yes';
$PREF{default_filelist_mode}				= 'list'; # list or grid.
$PREF{num_columns_in_grid_mode}				= 3;
$PREF{show_options_menu}				= 'yes';
$PREF{name_of_top_level}				= 'uploads';



# PREFs Section 11: File-List Configuration.
############################################################################
# You can enable a "Save" link on the "options" menu for each file in the
# file list.  This is just like the normal download link that you get when
# you click on a filename in the file list, except that instead of being a
# direct link to the target file on the server, it's a link that goes through
# FileChucker and forces the browser to treat it as a file download, instead
# of trying to display the file (i.e. for an image) or run a plugin on it
# (i.e. for a movie file).  Set this to null ('') to disable it.
#
$PREF{enable_save_link}					= 'Download';



# PREFs Section 11: File-List Configuration.
############################################################################
# Pagination settings, in case you have lots of files/folders which aren't
# spread across a lot of subfolders, so your individual pages are very big.
#
$PREF{num_items_per_page_on_filelist}			= 100;
$PREF{filelist_itemname_singular}			= 'item';
$PREF{filelist_itemname_plural}				= 'items';
$PREF{filelist_pagename_singular}			= 'page';
$PREF{filelist_pagename_plural}				= 'pages';
$PREF{filelist_pagination_links_template}		= qq`
	<div class="pagelinks">

	%%%ifelse-frstlink%%% <a href="%%frstlink%%">&lt;&lt;</a> %%%else%%% &lt;&lt; %%%endelse-frstlink%%%
	%%%ifelse-prevlink%%% <a href="%%prevlink%%">&lt;</a>     %%%else%%% &lt;     %%%endelse-prevlink%%%

	%%%template:linklist%%%
		%%%ifelse-currentpage%%%
			<span class="current">%%pagenum%%</span>
		%%%else%%%
			<a href="%%link%%">%%pagenum%%</a>
		%%%endelse-currentpage%%%
	%%%end-template:linklist%%%

	%%%ifelse-nextlink%%% <a href="%%nextlink%%">&gt;</a>     %%%else%%% &gt;     %%%endelse-nextlink%%%
	%%%ifelse-lastlink%%% <a href="%%lastlink%%">&gt;&gt;</a> %%%else%%% &gt;&gt; %%%endelse-lastlink%%%

	<div style="margin-top: 10px;">(%%num_items%% %%itemname%% on %%num_pages%% %%pagename%%)</div>
	</div>
`;



# PREFs Section 11: File-List Configuration.
############################################################################
# Miscellaneous self-explanatory settings.
#
$PREF{show_size_column_in_filelist}			= 'yes';
$PREF{show_date_column_in_filelist}			= 'yes';
$PREF{hide_file_extensions_in_filelist___from_first_dot}= 'no';
$PREF{hide_file_extensions_in_filelist___from_last_dot}	= 'no';
$PREF{default_filelist_sort}				= 'n'; # options: n,s,d,nr,sr,dr [name,size,date (reverse)].



# PREFs Section 11: File-List Configuration.
############################################################################
# If you've enabled the $PREF{store_upload_info_in_database} option (see
# PREFs Section 09) then you can choose to display data from your uploads as
# columns in the file list.  The variables are of the form %%varname%% where
# varname can be any of your _shortname values from any $PREF{formfield_NN}
# options (PREFs Section 07), or any of the built-in variables listed in 
# PREFs Section 09 with the $PREF{store_upload_info...} options.
#
#$PREF{custom_filelist_column_code__header}		= qq`<th>Info</th>`;
#$PREF{custom_filelist_column_code__folders}		= qq`<td class="cinfo"></td>`;
#$PREF{custom_filelist_column_code__files}		= qq`<td class="cinfo">%%ip%%</td>`;



# PREFs Section 11: File-List Configuration.
############################################################################
# Choose whether to display a checkbox at the end of each row, and a 
# drop-down list of actions at the bottom of the form, to allow users to
# perform actions on multiple files/folders at the same time.
#
# Also choose whether to enable the file/folder/size stats in the footer.
#
# For $PREF{multidownload_command_template} you may need to specify the full
# path to the zip command (e.g. /usr/bin/zip or /usr/local/bin/zip).
#
$PREF{enable_summary_of_counts_and_sizes}		= 'yes';
$PREF{enable_item_action_checkboxes}			= 'yes';
$PREF{enable_unzip_action}				= 'Unzip'; # this feature is in progress and incomplete.
$PREF{enable_delete_action}				= 'Delete'; # null to disable.
#
$PREF{enable_multidownload_action}			= 'Download'; # null to disable.
$PREF{multidownload_output_filename_template}		= '%ENV{SERVER_NAME}_download_%DATE{%Y%m%d-%H%M}.zip';
$PREF{multidownload_command_template}			= 'zip -q -r %%output_filename%% %%input_file_list%% -x \*fcziptmp\* -x \*fcimages\*';
$PREF{automatically_delete_old_multidownload_zip_files}	= 'yes';
$PREF{max_age_for_multidownload_zip_files}		= '48'; # In hours, but can be fractional (decimal).



# PREFs Section 11: File-List Configuration.
############################################################################
# You can specify different thumbnail icons to be shown for different types
# of files, based on their extensions.  You must provide the icon files 
# yourself, by putting them in a folder on your server (say, /icons/) and
# then specifying them here.  For example:
#
#$PREF{mimetype_icon_for_pdf}				= '/icons/pdf_icon.jpg';
#$PREF{mimetype_icon_for_doc}				= '/icons/ms_doc_icon.png';
#$PREF{mimetype_icon_for_mpg}				= '/icons/movie_file_icon.gif';
#$PREF{mimetype_icon_for_avi}				= '/icons/movie_file_icon.gif';
#$PREF{mimetype_icon_for_mov}				= '/icons/movie_file_icon.gif';



# PREFs Section 11: File-List Configuration.
############################################################################
# If you've set $PREF{store_upload_info_in_database} in PREFs Section 09,
# each file in your file list will have an "info" link that displays some
# information about the file and about the upload session that sent it.
# Here you can specify what the info page looks like.  By default it starts
# with all the built-in data fields collected, and then includes the special
# variable %%formfields%% which includes any form fields that you have enabled
# (see PREFs Section 07).  You can also display your own form fields here
# manually, by using the variable %%shortname%%, where "shortname" is what
# you've set for the $PREF{formfield_NN_shortname} option in PREFs Section 07.
#
$PREF{file_info_page_template} = qq`
	<table id="fcinfo">

	<tr><td class="f">Current filename:</td>				<td class="v">%%filepath%%%%filename%%</td></tr>
	<tr><td class="f">Original filename:</td>				<td class="v">%%origpath%%%%origname%%</td></tr>
	<tr><td class="f">File size:</td>					<td class="v">%%filesize%%</td></tr>
	<tr><td class="f">Uploaded in a group of this many files:</td>		<td class="v">%%filecount%%</td></tr>
	<tr><td class="f">Total upload size:</td>				<td class="v">%%uploadsize%%</td></tr>
	<tr><td class="f">Upload serial number:</td>				<td class="v">%%serial%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	<tr><td class="f">Uploader's IP address:</td>				<td class="v">%%ip%%</td></tr>
	<tr><td class="f">Uploader's hostname:</td>				<td class="v">%%host%%</td></tr>
	<tr><td class="f">Uploader's user dir:</td>				<td class="v">%%userdir%%</td></tr>
	<tr><td class="f">Uploader's username:</td>				<td class="v">%%username%%</td></tr>
	<tr><td class="f">Uploader's user agent:</td>				<td class="v">%%useragent%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	<tr><td class="f">Start time for entire upload:</td>			<td class="v">%%starttime%%</td></tr>
	<tr><td class="f">End time for entire upload:</td>			<td class="v">%%endtime%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	<tr><td class="f">Start etime for entire upload:</td>			<td class="v">%%startetime%%</td></tr>
	<tr><td class="f">End etime for entire upload:</td>			<td class="v">%%endetime%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	<tr><td class="f">Elapsed time in seconds for entire upload:</td>	<td class="v">%%elapsecs%%</td></tr>
	<tr><td class="f">Elapsed time in minutes for entire upload:</td>	<td class="v">%%elapmins%%</td></tr>
	<tr><td class="f">Elapsed time in hours for entire upload:</td>		<td class="v">%%elaphours%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	<tr><td class="f">Upload counter number:</td>				<td class="v">%%counternum%%</td></tr>
	<tr><td colspan="2" class="spacer"></td></tr>

	%%%if-formfields%%%
	<tr><td colspan="2" class="h">Form Field Entries:</td></tr>
	%%formfields%%
	%%%end-formfields%%%

	</table>
`;



# PREFs Section 11: File-List Configuration.
############################################################################
# File-list styling.  Set the color the rows change to on mouse-over (and
# on mouse-out); choose the default file-list style and whether to display 
# a link in the footer to switch between the styles.  You can also create
# your own styles here by adding the name of your new style to the list in
# the enabled_styles PREF, adding a block of corresponding PREFs for it
# here, and then adding a section for it in PREFs Section 16.
#
# Note: the "round", "dark", and "big" styles have been disabled due to
# incompatibilities with some recent markup changes; they will be updated
# or removed/replaced in a future update.
#
$PREF{default_filelist_style}				= 'shadowlight';
$PREF{enable_filelist_style_switcher}			= 'yes';
$PREF{enabled_styles}					= 'shadowdark, shadowlight, light';

$PREF{round___filelist_row_hover_bgcolor}		= '#c0c2b9';
$PREF{round___filelist_row_hover_bgcolor_highcontrast}	= '#86a9bc';
$PREF{round___filelist_row_normal_bgcolor_even}		= '#efefef';
$PREF{round___filelist_row_normal_bgcolor_odd}		= '#efefef';
$PREF{round___filelist_row_hover_text_color}		= 'white';
$PREF{round___filelist_row_hover_link_color}		= 'white';
$PREF{round___filelist_row_normal_text_color}		= '#444';
$PREF{round___filelist_row_normal_link_color}		= '#444';
$PREF{round___filelist_row_visited_link_color}		= '#444';
$PREF{round___filelist_row_highlight_bgcolor}		= '#88d984';

$PREF{light___filelist_row_hover_bgcolor}		= '#c0c2b9';
$PREF{light___filelist_row_hover_bgcolor_highcontrast}	= '#507090';
$PREF{light___filelist_row_normal_bgcolor_even}		= '#efefef';
$PREF{light___filelist_row_normal_bgcolor_odd}		= '#e6e6e6';
$PREF{light___filelist_row_hover_text_color}		= 'white';
$PREF{light___filelist_row_hover_link_color}		= 'white';
$PREF{light___filelist_row_normal_text_color}		= 'black';
$PREF{light___filelist_row_normal_link_color}		= 'black';
$PREF{light___filelist_row_visited_link_color}		= 'black';
$PREF{light___filelist_row_highlight_bgcolor}		= '#5cae64';

$PREF{shadowdark___filelist_row_hover_bgcolor}		= '#c0c2b9';
$PREF{shadowdark___filelist_row_hover_bgcolor_highcontrast}	= '#507090';
$PREF{shadowdark___filelist_row_normal_bgcolor_even}	= '#efefef';
$PREF{shadowdark___filelist_row_normal_bgcolor_odd}	= '#e6e6e6';
$PREF{shadowdark___filelist_row_hover_text_color}	= 'white';
$PREF{shadowdark___filelist_row_hover_link_color}	= 'white';
$PREF{shadowdark___filelist_row_normal_text_color}	= 'black';
$PREF{shadowdark___filelist_row_normal_link_color}	= 'black';
$PREF{shadowdark___filelist_row_visited_link_color}	= 'black';
$PREF{shadowdark___filelist_row_highlight_bgcolor}	= '#5cae64';

$PREF{shadowlight___filelist_row_hover_bgcolor}		= '#c0c2b9';
$PREF{shadowlight___filelist_row_hover_bgcolor_highcontrast}	= '#507090';
$PREF{shadowlight___filelist_row_normal_bgcolor_even}	= '#efefef';
$PREF{shadowlight___filelist_row_normal_bgcolor_odd}	= '#e6e6e6';
$PREF{shadowlight___filelist_row_hover_text_color}	= 'white';
$PREF{shadowlight___filelist_row_hover_link_color}	= 'white';
$PREF{shadowlight___filelist_row_normal_text_color}	= 'black';
$PREF{shadowlight___filelist_row_normal_link_color}	= 'black';
$PREF{shadowlight___filelist_row_visited_link_color}	= 'black';
$PREF{shadowlight___filelist_row_highlight_bgcolor}	= '#5cae64';

$PREF{dark___filelist_row_hover_bgcolor}		= '#474747';
$PREF{dark___filelist_row_normal_bgcolor_even}		= '#545454';
$PREF{dark___filelist_row_normal_bgcolor_odd}		= '#545454';
$PREF{dark___filelist_row_hover_text_color}		= 'white';
$PREF{dark___filelist_row_hover_link_color}		= '#000';
$PREF{dark___filelist_row_normal_text_color}		= '#fff';
$PREF{dark___filelist_row_normal_link_color}		= '#fff';
$PREF{dark___filelist_row_visited_link_color}		= '#fff';
$PREF{dark___filelist_row_highlight_bgcolor}		= '#aa3333';

$PREF{darker___filelist_row_hover_bgcolor}		= '#4a774a';
$PREF{darker___filelist_row_normal_bgcolor_even}	= '#545454';
$PREF{darker___filelist_row_normal_bgcolor_odd}		= '#4d4d4d';
$PREF{darker___filelist_row_hover_text_color}		= 'white';
$PREF{darker___filelist_row_hover_link_color}		= 'white';
$PREF{darker___filelist_row_normal_text_color}		= '#fff';
$PREF{darker___filelist_row_normal_link_color}		= '#fff';
$PREF{darker___filelist_row_visited_link_color}		= '#fff';

$PREF{big___filelist_row_hover_bgcolor}			= '#507090';
$PREF{big___filelist_row_hover_bgcolor_highcontrast}	= '#507090';
$PREF{big___filelist_row_normal_bgcolor_even}		= '#efefef';
$PREF{big___filelist_row_normal_bgcolor_odd}		= '#e6e6e6';
$PREF{big___filelist_row_hover_text_color}		= 'black';
$PREF{big___filelist_row_hover_link_color}		= 'black';
$PREF{big___filelist_row_normal_text_color}		= 'black';
$PREF{big___filelist_row_normal_link_color}		= 'black';
$PREF{big___filelist_row_visited_link_color}		= 'black';
$PREF{big___filelist_row_highlight_bgcolor}		= '#5cae64';

$PREF{minimal___filelist_row_hover_bgcolor}		= '#a3a3a3';
$PREF{minimal___filelist_row_normal_bgcolor_even}	= '#fff';
$PREF{minimal___filelist_row_normal_bgcolor_odd}	= '#fff';
$PREF{minimal___filelist_row_hover_text_color}		= 'black';
$PREF{minimal___filelist_row_hover_link_color}		= 'black';
$PREF{minimal___filelist_row_normal_text_color}		= 'black';
$PREF{minimal___filelist_row_normal_link_color}		= 'black';
$PREF{minimal___filelist_row_visited_link_color}	= 'black';



# PREFs Section 11: File-List Configuration.
############################################################################
# If you have userdirs enabled (see PREFs Section 04), and you don't have
# any top-level folders other than the home folder which contains the 
# userdirs, then you may want to automatically place your users into their
# home folders when they're viewing the file-list, since there's nothing
# else for them to see at the top level.
#
# You can also choose to hide the userdir folder name (usually "home") in
# the breadcrumbs at the top of the filelist, i.e. the default is this:
#
#	Viewing: / uploads / home / username /
#
# ...but instead display this:
#
#	Viewing: / uploads / username /
#
# And you can set $PREF{hide_links_to_topmost_level_from_userdir_users}
# if you want to suppress the "uploads" portion of the Viewing: line.
#
$PREF{navigate_users_into_userdirs_automatically}	= 'yes';
$PREF{hide_userdir_folder_name_in_breadcrumbs}		= 'yes';
$PREF{hide_links_to_topmost_level_from_userdir_users}	= 'no';
$PREF{hide_leading_slash_in_breadcrumbs}		= 'yes';
$PREF{hide_trailing_slash_in_breadcrumbs}		= 'yes';



# PREFs Section 11: File-List Configuration.
############################################################################
# The links to download files can either be normal HTML links that go
# directly to the file:
#
#	<a href="/path/to/uploads/blah/myfile.foo">myfile.foo</a>
#
# ...or, they can go through FileChucker:
#
#	<a href="/upload/?action=download&path=blah&file=myfile.foo">myfile.foo</a>
#
# If the links go through FileChucker, then FileChucker can also do other
# things like password-protect them (via $PREF{groups_allowed_to_download)),
# send email notifications whenever a file is downloaded, log downloads, etc.
# Whenever one of those features is enabled, FileChucker will internally
# automatically enable $PREF{download_links_go_through_FileChucker}.
#
# Note that the download_links_go_through_FileChucker option is mutually
# exclusive with the download_links_go_through_PeerFactor option.
#
$PREF{download_links_go_through_FileChucker}		= 'no';
$PREF{update_timestamp_on_download}			= 'no';
$PREF{log_all_downloads}				= 'no';
$PREF{download_log_table}				= 'download_info'; # will be created automatically.



# PREFs Section 11: File-List Configuration.
############################################################################
# You can prevent other sites from hotlinking your files by specifying a
# whitelist of allowed hotlinking domains here.  This is commented-out by
# default, which means that hotlinking is allowed from all sites.
#
# $ENV{HTTP_HOST} is (usually) set to your domain name, i.e. yoursite.com,
# so if you uncomment the default setting, then only your own site will be
# able to link to your files.
#
# Do not include http:// or https:// or www. in your domains here, and do
# not put a slash at the end of the domain name.
#
#$PREF{hotlink_whitelist}{'01'}				= $ENV{HTTP_HOST};



# PREFs Section 11: File-List Configuration.
############################################################################
# You can choose to have your download links go through PeerFactor, which
# is a P2P-based automatic load-balancing system.  All the links in your
# file-list will get prefixed with:
#
#	http://www.peerfactor.fr/get_myfile.jsp?URL=
#
# When a user clicks on a download link, he will receive the file from the
# PeerFactor P2P network if demand for that file is high, or else he'll get
# the file directly from your server if demand for the file is low.  The
# PeerFactor site determines demand in real-time so this is all transparent
# to the user.
#
# Note that the download_links_go_through_PeerFactor option is mutually
# exclusive with the download_links_go_through_FileChucker option.
#
$PREF{download_links_go_through_PeerFactor}		= 'no';



# PREFs Section 11: File-List Configuration.
############################################################################
# You can specify that your download links go to a landing page, instead of
# directly to the file, useful if you want to display ads on downloads, etc.
# You can optionally enable the landing page only in some contexts, for 
# example on the "upload complete" page but not the file list.  If you don't
# explicitly set those context-based versions, they'll take the value of the
# main $PREF{downloads_use_landing_page} setting.
# 
$PREF{downloads_use_landing_page}			= 'no';
#$PREF{downloads_use_landing_page___uploadcomplete}	= 'no';
#$PREF{downloads_use_landing_page___filelist}		= 'no';
#$PREF{downloads_use_landing_page___email}		= 'no';
$PREF{landing_page_delay}				= 0; # in seconds.
$PREF{landing_page_wait_message}			= qq`<p>Your download link will be displayed in %%delay%% seconds; please wait.</p>`;
$PREF{landing_page_title}				= qq`Download File`;
$PREF{landing_page_template}				= qq`
<h2>Download File:</h2>
%%extra_message%%
%%%delay-wrapper%%%
	<p><a href="%%url%%">%%filename%%</a> (%%size%%)</p>
%%%end-delay-wrapper%%%
`;



# PREFs Section 11: File-List Configuration.
############################################################################
# You can choose to have FileChucker automatically delete files older than
# a set number of hours.  Set the max_age_for_uploads to the age (in
# hours) at which you'd like old files to get deleted.  In order to delete
# old files, we need to check the age of all the files every N hours or
# minutes.  You can choose to make this check happen daily (at a certain
# hour/hours) or hourly (at a certain minute/minutes).  For the lists of
# hours/minutes at which to check, the numbers must be separated by commas
# and/or spaces.
#
# Note that a file's date/timestamp is only updated when the file is
# created or modified; it is NOT updated when the file is simply accessed
# (i.e. by being downloaded).  If you want the date/timestamps to get
# updated upon download, then you must set update_timestamp_on_download
# in PREFs Section 11.
# 
# Finally, note that in order for this to work, the script must actually be
# running at the hour(s) or minute(s) that you specify, i.e. someone must 
# happen to be either uploading a file at that time, or viewing the file-
# list at that time.  So if your FileChucker installation doesn't get very
# many visitors, you will probably want to use the "check_daily" option
# instead of the "check_hourly" one, and you'll want to specify a bunch of
# different hours at which to check.  For example, you could list every
# hour from 0 to 23 (and enable "check_daily_for_old_files") to cause 
# FileChucker to perform this check every single time it runs.  Of course
# on servers with lots of traffic, you wouldn't want to run the check
# that often.
# 
$PREF{automatically_delete_old_uploads}			= 'no';
$PREF{automatically_delete_old_logfiles}		= 'yes';
$PREF{max_age_for_uploads}				= '168'; # In hours, but can be fractional (decimal).
$PREF{max_age_for_logfiles}				= '72'; # In hours, but can be fractional (decimal).
$PREF{check_daily_for_old_files}			= 'yes';
$PREF{hours_at_which_to_check}				= '0,6,12,18'; # can be from 0 to 23.
$PREF{check_hourly_for_old_files}			= 'no';
$PREF{minutes_at_which_to_check}			= '0,15,30,45'; # can be from 0 to 59.



# PREFs Section 11: File-List Configuration.
############################################################################
# Configure your upload log and download log pages.  To enable the upload
# log, you must enable the $PREF{store_upload_info_in_database} setting in
# PREFs Section 09, and to enable the download log you must enable the
# $PREF{log_all_downloads} setting above.  Both logs require that you set
# the database settings in PREFs Section 12.
#
$PREF{upload_log_viewer_title}				= 'Upload Log';
$PREF{upload_log_viewer_template}			= qq`<h2>Upload Log</h2>\n<br />\n<p>[ %%horizlink:text=Horizontal%% | %%vertlink:text=Vertical%% %%%if-viewall%%% | %%viewalllink:text=View All%% %%%end-viewall%%% ]</p>\n<p>%%pagelinks%%</p>\n\n<br />\n%%output%%\n<p>%%pagelinks%%</p>\n`;
$PREF{upload_log_viewer_hidden_columns}			= 'origname,origpath,endtime,startetime,endetime,elaphours,elapsecs,serial,userdir,filecount,uploadsize,counternum,useragent,ip';
$PREF{upload_log_viewer_disabled_columns}		= '';
$PREF{upload_log_viewer_max_display_length}		= 20;
$PREF{upload_log_viewer_itemsperpage}			= 25;
#
$PREF{download_log_viewer_title}			= 'Download Log';
$PREF{download_log_viewer_template}			= qq`<h2>Download Log</h2>\n<br />\n<p>[ %%horizlink:text=Horizontal%% | %%vertlink:text=Vertical%% %%%if-viewall%%% | %%viewalllink:text=View All%% %%%end-viewall%%% ]</p>\n<p>%%pagelinks%%</p>\n\n<br />\n%%output%%\n<p>%%pagelinks%%</p>\n`;
$PREF{download_log_viewer_hidden_columns}		= 'userdir,useragent,etime';
$PREF{download_log_viewer_disabled_columns}		= '';
$PREF{download_log_viewer_max_display_length}		= 20;
$PREF{download_log_viewer_itemsperpage}			= 25;



# PREFs Section 11: File-List Configuration.
############################################################################
# Configure your download notification email.  This requires that you set
# the SMTP/sendmail/etc preferences in PREFs Section 06.
#
$PREF{send_download_notification_emails}		= 'no';
$PREF{download_notification_email_recipient_1}		= 'me@example.com';
$PREF{download_notification_email_subject}		= "File download: %%filename%%";
#
$PREF{download_notification_email_template} = qq`
<h1>File Download Notification</h1>
<p>File: <a href="%%linktofile%%">%%filename%%</a> (%%filesize%%)</p>

<p><br /></p><hr />
<h2>Technical Info:</h2>
<p>Download date: %%date%%</p>
<p>Downloader's IP Address: %%ip%%</p>
<p>Downloader's Hostname: %%host%%</p>
<p>Downloader's User-Agent: %%ua%%</p>
<p>Downloader's User-Dir: %%userdir%%</p>
<p>Downloader's Username: %%username%%</p>

<p><br /></p><hr />
<p>This message sent by FileChucker at:</p>
<p><a href="$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}">$PREF{protoprefix}$ENV{HTTP_HOST}$PREF{here}</a></p>
`;



# PREFs Section 11: File-List Configuration.
############################################################################
# Shopping cart / ordering system: you can enable a very basic ordering
# system, where your users can select items (files) from your upload area
# and add them to their cart, and they can then place an order for those
# items, which simply sends an email to you, containing their user info
# and the list of items that they selected.  Note that you must configure
# the SMTP settings in PREFs Section 06 for this to work.
#
$PREF{enable_ordering}					= 'no';
$PREF{select_item_link}					= qq`<span style="white-space: nowrap;">Add To Cart</span>`; # no single-quotes within this setting.
$PREF{selection_cookie_name}				= 'selected_items';
$PREF{clear_selections_text}				= 'Empty Cart';
$PREF{clear_selections_verification_text}		= 'About to empty your cart.  Is that OK?';
$PREF{no_selections_text}				= 'Your cart is empty.';
$PREF{item_added_to_cart_text}				= 'Item added to cart.';
$PREF{duplicate_item_text}				= 'This item is already in your cart.  Add it again?';

$PREF{view_items_page_name}				= 'Your Cart';
$PREF{view_items_page_intro}				= '<h1>Your Cart</h1><p>Your cart contains the following items.&nbsp; Use the Submit<br />button below when you are ready to checkout.</p>';
$PREF{place_order_fields}				= '<div class="name"><input type="text" name="name" class="text required" /> Name</div> <div class="email"><input type="text" name="email" class="text required" /> Email</div> <div class="submit"><input type="button" value="Submit Your Order" class="default button" onclick="startorder()" /></div> ';

$PREF{process_order_page_name}				= 'Order Received - Thank You';
$PREF{process_order_page_intro}				= '<h1>Order Received</h1><p>Thank you for your order.&nbsp; We are now processing it and we will <br />contact you soon.&nbsp; Please print or save this page for your records.</p>';

$PREF{order_email_recipient_1}				= 'me@example.com';
$PREF{order_sender_email_address}			= 'orderform@example.com';
$PREF{order_email_subject}				= 'Order Received';
$PREF{order_email_top_intro}				= '<h1>Order Received:</h1>';
$PREF{order_email_items_intro}				= '<h2>Items Ordered:</h2>';
$PREF{order_email_user_intro}				= '<h2>User Information:</h2>';
$PREF{send_copy_to_userEntered_email_address}		= 'yes';









# PREFs Section 12: Database Setup.
############################################################################
# If you're using any FileChucker features that require a database, then
# you'll need to configure it here.  The hostname may be left blank (which
# defaults to 'localhost') on many servers, but the other three settings --
# database name, username, and password -- must be specified.
#
# The database user needs at least the INSERT and SELECT privileges, but
# depending on which DB-related PREFs you're using, it may need other privs
# too (see that particular PREF for the details).
#
# Set $PREF{reconnect_to_db_after_upload} if your server reports "lost
# connection to MySQL server..." after your uploads finish.
#
$PREF{database_hostname}				= '';
$PREF{database_name}					= '';
$PREF{database_username}				= '';
$PREF{database_password}				= '';
$PREF{reconnect_to_db_after_upload}			= 'yes';
#
# The following setting usually doesn't need to be adjusted.  If you're
# using PostgreSQL instead of MySQL, then just make sure you have the
# DBD::Pg Perl module installed, then change the dbi_connection_string
# to "dbi:Pg:dbname=%%dbname%%".  Or if your mysql.sock file is in a
# non-standard location, you can specify that in the connection string:
#
#	dbi:mysql:%%dbname%%;mysql_socket=/var/mysql/mysql.sock
#
$PREF{dbi_connection_string}				= "dbi:mysql:%%dbname%%";










# PREFs Section 13: Internationalization and Localization.
############################################################################
# For internationalization and localization (i18n and l10n).  Modify *only*
# the right-hand side of each statement to translate the string into another
# language.
#
# Note that not quite everything is i18n/l10n'able yet, so you may have to
# modify the text directly in the code itself to change some strings.  Also
# note that some strings are already adjustable via a $PREF{foo} option
# above, so those need to be adjusted there instead of here in a $TEXT{foo}
# setting.
#
$TEXT{Actions_Menu}						= qq`Actions Menu`;
$TEXT{Add_another_file_}					= qq`Add another file?`;
$TEXT{Administration}						= qq`Administration`;
$TEXT{and}							= qq`and`;
$TEXT{Apply}							= qq`Apply`;
$TEXT{Are_you_sure_you_want_to_delete_it___}			= qq`Are you sure you want to delete it and all its contents?`;
$TEXT{Are_you_sure_you_want_to_delete_this___}			= qq`Are you sure you want to delete this item?`;
$TEXT{Average_speed}						= qq`Average speed`;

$TEXT{boolean_false_string}					= 'no';
$TEXT{boolean_true_string}					= 'yes';
$TEXT{but_there_were_errors}					= qq`but there were errors`;

$TEXT{checkbox_yes}						= qq`yes`;
$TEXT{checkbox_no}						= qq`no`;
$TEXT{Check_Image_Modules}					= qq`Check Image Modules`;
$TEXT{click_here}						= qq`click here`;
$TEXT{_Close_Menu_}						= qq`[Close Menu]`;
$TEXT{Completed}						= qq`Completed`;
$TEXT{Configuration}						= qq`Configuration`;
$TEXT{Connecting_please_wait_}					= qq`Connecting; please wait.`;
$TEXT{Contents_}						= qq`Contents:`;
$TEXT{Copied}							= qq`Copied`;
$TEXT{Copy}							= qq`Copy`;
$TEXT{Copy_It}							= qq`Copy It`;
$TEXT{Copying}							= qq`Copying`;
$TEXT{Current_filename_}					= qq`Current filename:&nbsp; `;

$TEXT{database_create_button}					= qq`Add new %%itemname%%`;
$TEXT{database_create_button_2}					= qq`Save new %%itemname%%`;
$TEXT{database_delete_successful}				= qq`Successfully deleted the %%itemname%%.`;
$TEXT{database_deleter_title}					= qq`Or you can delete this %%itemname%%:`;
$TEXT{database_deleter_checkbox}				= qq`Check this box to confirm that you want to delete the %%itemname%%.`;
$TEXT{database_deleter_button}					= qq`Delete this %%itemname%%`;
$TEXT{database_save_button}					= qq`Save changes`;
$TEXT{Date}							= qq`Date`;
$TEXT{days}							= qq`days`;
$TEXT{Delete}							= qq`Delete`;
$TEXT{Delete_now_including_any_folder_contents_}		= qq`Delete now (including any folder contents)?`;

$TEXT{Edit}							= qq`Edit`;
$TEXT{Elapsed_time}						= qq`Elapsed time`;
$TEXT{Elapsed_time_in_hours_for_entire_upload_}			= qq`Elapsed time in hours (for entire upload):   `;
$TEXT{Elapsed_time_in_minutes_for_entire_upload_}		= qq`Elapsed time in minutes (for entire upload): `;
$TEXT{Elapsed_time_in_seconds_for_entire_upload_}		= qq`Elapsed time in seconds (for entire upload): `;
$TEXT{End_etime_for_entire_upload_}				= qq`End etime (for entire upload):   `;
$TEXT{End_time_for_entire_upload_}				= qq`End time (for entire upload):   `;
$TEXT{Enter_password_for_file}					= qq`Enter the password to download this file:`;
$TEXT{Enter_the_password}					= qq`Enter your password:`;
$TEXT{Error__failed_human_test__please_try_again_}		= qq`Error: failed human test; please try again.`;
$TEXT{Error_illegal_filename_}					= qq`Error: illegal filename.`;
$TEXT{Error_URL_missing_userdir}				= qq`Error: malformed URL; you need to pass userdir=yourusername on the URL.`;

$TEXT{file}							= qq`file`;
$TEXT{File}							= qq`File`;
$TEXT{Files}							= qq`Files`;
$TEXT{files}							= qq`files`;
$TEXT{File_size_}						= qq`File size: `;
$TEXT{filepw_access_denied}					= qq`Access denied: invalid password.`;
$TEXT{filepw_button_label}					= qq`Submit`;
$TEXT{folder}							= qq`folder`;
$TEXT{folders}							= qq`folders`;
$TEXT{Folder_Thumbs_}						= qq`Folder Thumbs:`;
$TEXT{Forgot_password_}						= qq`<p><br />[ <a href="http://encodable.com/filechucker/faq/#password">Forgot password?</a> ]</p>`;
$TEXT{From_}							= qq`From:`;

$TEXT{Go}							= qq`Go`;
$TEXT{grid}							= qq`grid`;

$TEXT{Help}							= qq`Help`;
$TEXT{hour}							= qq`hour`;
$TEXT{hours}							= qq`hours`;
$TEXT{HTML_}							= qq`HTML code: `;
$TEXT{Human_test__type_the_numbers_in_the_box_}			= qq`Human test: type the numbers in the box:`;

$TEXT{images}							= qq`images`;
$TEXT{Image_Thumbs_}						= qq`Image Thumbs:`;
$TEXT{In_}							= qq`In:`;
$TEXT{_incl_subfolders_}					= qq`(incl. subfolders)`;
$TEXT{Info}							= qq`Info`;
$TEXT{Insufficient_permissions_to_download_file_}		= qq`Insufficient permissions to download file.`;
$TEXT{Invalid_Login}						= qq`Invalid Login`;
$TEXT{item}							= qq`item`;
$TEXT{items}							= qq`items`;

$TEXT{Keep_me_logged_in_for}					= qq`Keep me logged in for`;

$TEXT{Layout_}							= qq`Layout:`;
$TEXT{_left_blank_by_user_}					= qq`(left blank by user)`;
$TEXT{Link_}							= qq`Link: `;
$TEXT{list}							= qq`list`;
$TEXT{Logging_out_}						= qq`Logging out;`;
$TEXT{Login}							= qq`Login`;
$TEXT{Logout}							= qq`Logout`;

$TEXT{minute}							= qq`minute`;
$TEXT{minutes}							= qq`minutes`;
$TEXT{Move}							= qq`Move`;
$TEXT{Move_It}							= qq`Move It`;
$TEXT{Move_Rename}						= qq`Move/Rename`;
$TEXT{Moved}							= qq`Moved`;
$TEXT{Moving}							= qq`Moving`;
$TEXT{multidownload_warning}					= qq`You have selected a multi-item download, which means we will need to zip them into a single zip file for you.  This may take some time if there are many files or large files.  Do you want to continue?`;
$TEXT{My_Account}						= qq`My Account`;

$TEXT{Name}							= qq`Name`;
$TEXT{New_Folder}						= qq`New Folder`;
$TEXT{New_subdirectory__Name_}					= qq`New subfolder? Name:`;
$TEXT{no}							= qq`no`;
$TEXT{No_hotlinking_}						= qq`No hotlinking.`;
$TEXT{no_output_from_database}					= qq`<div style="text-align: center; font-style: italic;">(none)</div>`;
$TEXT{_none_}							= qq`(none)`;

$TEXT{of}							= qq`of`;
$TEXT{off}							= qq`off`;
$TEXT{on}							= qq`on`;
$TEXT{options}							= qq`options`;
$TEXT{Options_Menu}						= qq`Options Menu`;
$TEXT{Or_}							= qq`Or:`;
$TEXT{Original_filename_}					= qq`Original filename: `;

$TEXT{page}							= qq`page`;
$TEXT{pages}							= qq`pages`;
$TEXT{Parent_Directory}						= qq`Parent Directory`;
$TEXT{password_not_set}						= qq`You must <a href="%%newpw_link%%">set your administrator password</a> first.`;
$TEXT{Password_Required}					= qq`Password Required`;
$TEXT{Passwords_do_not_match_}					= qq`Passwords do not match.`;
$TEXT{Permissions}						= qq`Permissions`;
$TEXT{Please_enter_a_number_}					= qq`Please enter a number.`;
$TEXT{Please_enter_a_valid_email_address_}			= qq`Please enter a valid email address.`;
$TEXT{Please_fill_in_the_required_items_}			= qq`Please fill in the required item(s).`;
$TEXT{Please_wait}						= qq`Please wait`;

$TEXT{Remaining}						= qq`Remaining`;
$TEXT{Rename}							= qq`Rename`;
$TEXT{Rename_It}						= qq`Rename It`;
$TEXT{Renamed}							= qq`Renamed`;
$TEXT{Renaming}							= qq`Renaming`;
$TEXT{Rotate_now_}						= qq`Rotate now?`;

$TEXT{second}							= qq`second`;
$TEXT{seconds}							= qq`seconds`;
$TEXT{Select}							= qq`Select`;
$TEXT{Selected_}						= qq`Selected:`;
$TEXT{Select_All}						= qq`Select: All`;
$TEXT{Select_None}						= qq`None`;
$TEXT{Server_Information}					= qq`Server Information`;
$TEXT{Size}							= qq`Size`;
$TEXT{Start_etime_for_entire_upload_}				= qq`Start etime (for entire upload): `;
$TEXT{Start_time_for_entire_upload_}				= qq`Start time (for entire upload): `;
$TEXT{Styles_}							= qq`Styles:`;
$TEXT{subfolders_including_any_hidden_items_}			= qq`subfolders (including any hidden items).`;

$TEXT{The_owner_of_this_site_has_set_the_limit_to}		= qq`The owner of this site has set the limit to`;
$TEXT{The_password_you_entered_is_incorrect___}			= qq`The password you entered is incorrect.<br />Go back and try again.`;
$TEXT{This_folder_contains}					= qq`This folder contains`;
$TEXT{Time}							= qq`Time`;
$TEXT{To_}							= qq`To:`;
$TEXT{to_continue_}						= qq`to continue.`;
$TEXT{Total}							= qq`Total`;
$TEXT{Total_upload_size}					= qq`Total upload size`;
$TEXT{Total_upload_size_}					= qq`Total upload size: `;

$TEXT{Unzip_now_}						= qq`Unzip now?`;
$TEXT{Upload_counter_number_}					= qq`Upload counter number: `;
$TEXT{upload_form_subdir_note_1}				= qq`(will use folder settings from first file)`;
$TEXT{upload_form_subdir_note_2}				= qq`(will use folder from first file)`;
$TEXT{upload_form_subdir_note_3}				= qq`(will use new folder name from first file)`;
$TEXT{upload_form_subdir_note_4}				= qq`(optional; may be left blank)`;
$TEXT{Upload_Info}						= qq`Upload Info`;
$TEXT{Upload_serial_number_}					= qq`Upload serial number:  `;
$TEXT{Upload_statistics_}					= qq`Upload statistics:`;
$TEXT{Upload_to_}						= qq`Upload to:`;
$TEXT{upload_too_big_error}					= qq`<h1>Error:</h1><p>You tried to send %%upload_size%%, but the owner of this site has set the limit to %%limit%%.&nbsp; <a href="#" onclick="reset_upload_form_after_size_error();return false">Click here</a> to choose a smaller file.</p>`;
$TEXT{Uploaded_in_a_group_of_this_many_files_}			= qq`Uploaded in a group of this many files: `;
$TEXT{uploaded_successfully_}					= qq`uploaded successfully.`;
$TEXT{Uploaders_Form_Field_Entries_}				= qq`Uploader's Form Field Entries:`;
$TEXT{Uploaders_hostname_}					= qq`Uploader's hostname:   `;
$TEXT{Uploaders_IP_address_}					= qq`Uploader's IP address: `;
$TEXT{Uploaders_username_}					= qq`Uploader's username:   `;
$TEXT{Uploaders_user_dir_}					= qq`Uploader's user-dir:   `;
$TEXT{Uploaders_user_agent_}					= qq`Uploader's user-agent: `;
$TEXT{Uploading_please_wait_}					= qq`&nbsp;&nbsp;Uploading; please wait.`;
$TEXT{URL_}							= qq`URL to file: `;

$TEXT{Video_Thumbs_}						= qq`Video Thumbs:`;
$TEXT{Viewing_}							= qq`Viewing:`;
$TEXT{View_Upload_Log}						= qq`View Upload Log`;
$TEXT{View_Download_Log}					= qq`View Download Log`;

$TEXT{will_be_created_inside___}				= qq`(created in the selected directory)`;

$TEXT{Your_upload_is_complete}					= qq`Your upload is complete`;
$TEXT{yes}							= qq`yes`;









# PREFs Section 14: Templates.
############################################################################
# You can adjust various templatable items here.
#
$PREF{success_message_template}					= qq`<h2>Success</h2>\n<p>%%message%%</p>\n`;
$PREF{notice_message_template}					= qq`<h2>Notice</h2>\n<p>%%message%%</p>\n`;
$PREF{error_message_template}					= qq`<h2>Error</h2>\n<p>%%message%%</p>\n`;
#
$PREF{titlebar_title___uploader}				= qq`Upload a file`;
$PREF{titlebar_title___popupstatus}				= qq``; # not currently used.
$PREF{titlebar_title___uploadcomplete}				= qq`Upload complete`;
$PREF{titlebar_title___filelist}				= qq`Uploaded Files`;
$PREF{titlebar_title___login}					= qq`Enter the password`;
$PREF{titlebar_title___error}					= qq``; # not currently used.
#
$PREF{formfield_template___text}				= qq`
<div class="fcfieldwrap clearfixtb %%prefname%% singleline">
<label class="upform_label">%%display_name%%</label>
<input type="%%type%%" name="%%name%%" id="formfield-%%name%%"
 class="upform_field text %%prefname%%%%required%%%%emailformat%%%%numeric%%%%password%%"
 value="%%presetvalue%%" %%readonly%% />
</div>
`;
#
$PREF{formfield_template___multiline}				= qq`
<div class="fcfieldwrap clearfixtb %%prefname%% multiline">
<label class="upform_label">%%display_name%%</label>
<textarea name="%%name%%" class="upform_field textarea %%prefname%%%%required%%"
 id="formfield-%%name%%" %%readonly%%>%%presetvalue%%</textarea>
</div>
`;
#
$PREF{formfield_template___radio}				= qq`
<div class="fcfieldwrap clearfixtb %%prefname%% radio">
<label class="upform_label">%%display_name%%</label>
<div class="radiobox">
%%radio_buttons%%
</div>
<div class="clear"></div>
</div>
`;
#
$PREF{formfield_template___radio___buttons}			= qq`
<input type="radio" id="formfield-%%name%%-%%value%%"
 class="%%prefname%%%%required%% radio"
 name="%%name%%" value="%%value%%" %%checked%% %%readonly%% />
<label for="formfield-%%name%%-%%value%%">%%label%%</label>
`;
#
$PREF{formfield_template___checkbox}				= qq`
<div class="fcfieldwrap clearfixtb %%prefname%% checkbox">
<label class="upform_label">%%display_name%%</label>
<input type="checkbox" id="formfield-%%name%%"
 class="upform_field checkbox %%prefname%%%%required%%"
 name="%%name%%" %%checked%% %%readonly%% />
</div>
`;
#
$PREF{administration_template}					= qq`<div class="encmenu">\n<div class="header"><span class="altcolor1">&gt;</span> Administration</div>\n<div>%%links%%</div></div>\n`;
#$PREF{extra_administration_links}				= [ '<a href="/foo">Foo</a>',  '<a href="/bar">Bar</a>' ];
#
$PREF{filefield_template} = qq`

<div id="firstfile" class="fcfieldwrap clearfixtb onesubgroup %%row_classname%% %%first_classname%% %%last_classname%%">
	<div class="upform_pair">
		<label class="upform_label" for="uploadname%%i%%">File <span class="filei">%%i%%</span> of <span class="fileitotal">%%numitems%%</span>:</label>
		<input type="file" size="15" class="upform_field file %%required_classname%%" name="uploadname%%i%%" id="uploadname%%i%%" %%auto_add_more_files%% />
	</div>

	%%%if-subdirs%%%

		%%%ifelse-choosesubdir%%%
			<div class="upform_pair">
				<label class="upform_label picksubdir_label">Upload to:</label>
				<select name="subdir%%i%%" class="upform_field picksubdir_field">
				%%%template:subdirlist%%%<option value="%%subdir_value%%" %%subdir_selected%%>%%subdir_displayname%%</option>%%%end-template:subdirlist%%%
				</select>
			</div>
		%%%else%%%
			<input type="hidden" name="subdir%%i%%" value="%%static_subdir%%" />
		%%%endelse-choosesubdir%%%

		%%%if-newdir%%%
			<div class="upform_pair">
				<label for="newsubdir%%i%%" class="upform_label newsubdir_label">%TEXT{New_subdirectory__Name_}</label>
				<input type="text" class="upform_field newsubdir_field default text" name="newsubdir%%i%%" id="newsubdir%%i%%" maxlength="%PREF{max_length_of_new_subdir_names}" title="%%newsubdir_instructions%%" />
			</div>
		%%%endif-newdir%%%

	%%%endif-subdirs%%%

	%%custom_perfile_code%%
	%%perfile_textboxes%%
</div>

`;










# PREFs Section 15: Image Options.
############################################################################
# FileChucker supports 3 image-based features: resizing (including small
# icon-type thumbnails images to represent the full-sized images),
# rotation, and a CAPTCHA-type human test.  To provide these features,
# FileChucker supports 4 different image tools: ImageMagick, GD, jpegtran,
# and convert.  Your server might have none, some, or all of these tools
# available.
#
#	ImageMagick: Perl module; supports rotation, resizing, and humantest.
#
#	GD: Perl module; supports rotation, resizing, and humantest, but does
#	not support the bitmap (*.bmp) file format.
#
#	jpegtran: system command; supports rotation but only for JPEG images,
#	and does not support resizing nor humantest.  For Windows servers,
#	download from http://sylvana.net/jpeg-bin/ and save jpegtran.exe somewhere
#	in your $PATH (like c:\Windows\).  Linux users, jpegtran is probably
#	included in your distro's package manager.
#
#	convert: system command; supports resizing, rotation, and humantest.
#	This is part of the ImageMagick suite (not the IM Perl module); download
#	from http://www.imagemagick.org/.  Note for Windows servers: Windows
#	has a built-in command called "convert" which is a disk utility, so
#	when you install ImageMagick, go into its Program Files folder and
#	make a copy of the convert.exe file, renaming the copy to something
#	else, like imgconv.exe, and then set $PREF{convert_command} = 'imgconv.exe'.
#	Note for Linux servers: if your convert binary is in /usr/local/bin
#	then you might need to specify the full path, because your $PATH may
#	not include that directory.
#
# The thumbnails are created automatically and cached in a hidden fcimages
# folder.  To force the regeneration of the thumbnails (i.e. update the
# cache) for a given folder, pass ?makethumbs=1 on the URL.  (Subject to
# security settings in PREFs Section 03.)
#
# The thumbnail size is specified according to ImageMagick's rules, namely:
# by default, the width and height are maximum values. That is, the image 
# is contracted to fit the width and height value while maintaining the 
# aspect ratio of the image. Append an exclamation point to the size to 
# force the image to exactly the size you specify.
#
# If only the width is specified, the width assumes the value and the 
# height is chosen to maintain the aspect ratio of the image. Similarly,
# if only the height is specified (e.g., 'x150'), the width is chosen to
# maintain the aspect ratio.
#
# If your server has GD but not ImageMagick, then the size rules are the
# same except that if both width and height are specified, then they are
# treated as absolute values, not maximum values, and the exclamation
# point has no effect.
#
$PREF{try_to_use_jpegtran_for_rotation}			= 'no';
$PREF{jpegtran_command}					= 'jpegtran'; # can optionally include path.

$PREF{try_to_use_convert_for_rotation}			= 'no';
$PREF{try_to_use_convert_for_resizing}			= 'no';
$PREF{try_to_use_convert_for_humantest}			= 'no';
$PREF{convert_command}					= 'convert'; # can optionally include path.

$PREF{try_to_use_identify_for_dimensions}		= 'no';
$PREF{identify_command}					= 'identify'; # can optionally include path.

$PREF{try_to_use_imagemagick_for_rotation}		= 'yes';
$PREF{try_to_use_imagemagick_for_resizing}		= 'yes';
$PREF{try_to_use_imagemagick_for_humantest}		= 'yes';
$PREF{try_to_use_imagemagick_for_dimensions}		= 'yes';

$PREF{try_to_use_gd_for_rotation}			= 'yes';
$PREF{try_to_use_gd_for_resizing}			= 'yes';
$PREF{try_to_use_gd_for_humantest}			= 'yes';
$PREF{try_to_use_gd_for_dimensions}			= 'yes';

# Experimental: uncomment this to try netpbm:
#$PREF{netpbm_command_for_humantest}			= qq`ppmmake %PREF{human_test_background_color} %PREF{human_test_image_width} %PREF{human_test_image_height} |ppmlabel -color %PREF{human_test_text_color} -size 12 -text %%random_number%% |ppmtojpeg >"%%output_filename%%"`;

$PREF{enable_rotate90_action}				= 'Rotate Right'; # set to null ('') to disable.
$PREF{enable_rotate180_action}				= 'Rotate 180 &deg;'; # set to null ('') to disable.
$PREF{enable_rotate270_action}				= 'Rotate Left'; # set to null ('') to disable.

$PREF{enable_file_thumbnails_in_filelist}		= 'yes';
$PREF{enable_folder_thumbnails_in_filelist}		= 'yes';
$PREF{visitors_can_toggle_thumbnails_on_and_off}	= 'yes';
$PREF{image_thumbnails_on_by_default}			= 'yes';
$PREF{folder_thumbnails_on_by_default}			= 'yes';
$PREF{max_image_size_to_resize}				= 1024*1024*8;
$PREF{filelist_thumbnail_size__imagemagick}		= '130x130';
$PREF{filelist_thumbnail_size__gd}			= '130';
$PREF{filelist_thumbnail_dir_name}			= 'fcimages';
#$PREF{prefix_for_thumbnailed_dir_names}		= qq`<b>Album:</b> `;
$PREF{filelist_thumbnail_image_extensions}		= '\.jpg$|\.jpeg$|\.png$|\.gif$|\.bmp$|\.jpe$'; # regular expression.
$PREF{resizable_image_extensions}			= '\.jpg$|\.jpeg$|\.png$|\.gif$|\.bmp$|\.jpe$'; # regular expression.
$PREF{rotatable_image_extensions}			= '\.jpg$|\.jpeg$|\.png$|\.gif$|\.bmp$|\.jpe$'; # regular expression.

$PREF{enable_video_thumbnails_in_filelist}		= 'yes';
$PREF{video_thumbnails_on_by_default}			= 'yes';
$PREF{video_thumbnail_dir_name}				= '%PREF{filelist_thumbnail_dir_name}';
$PREF{video_thumbnail_image_extensions}			= '\.asf$|\.avi$|\.flv$|\.mov$|\.mpeg$|\.mpg$|\.mp4$|\.wmv$|\.3gp$'; # regular expression.
$PREF{video_thumb_command}				= qq`ffmpeg -i "%%input_video_filename%%" -an -ss 00:00:03 -an -r 1 -vframes 1 -y "%%output_image_filename%%"`;
$PREF{ignore_video_thumbnailing_errors}			= 'yes'; # otherwise, corrupt/fake videos result in error messages.



# PREFs Section 15: Image Options.
############################################################################
# Separate from the thumbnail feature, FileChucker can automatically resize
# your uploaded images.  Or, it can create a copy of each uploaded image,
# and then resize that copy, leaving the original at its original size.
# 
# You can specify multiple sizes for resized copies by duplicating the
# create_resized_copies_01* PREFs and replacing the 01 with 02, 03, etc.
#
# For resized copies, you can specify that they're put into a subfolder,
# and/or that they are renamed.  If you don't want to put them into a
# subfolder, just set that PREF to null.
# 
$PREF{resize_uploaded_images}				= 'no';
$PREF{resize_uploaded_images__imagemagick_size}		= '800x800';
$PREF{resize_uploaded_images__gd_size}			= '800';

$PREF{create_resized_copies_of_uploaded_images}		= 'no';
$PREF{create_resized_copies_01__imagemagick_size}	= '800x800';
$PREF{create_resized_copies_01__gd_size}		= '800';
$PREF{create_resized_copies_01__subfolder_name}		= 'small';
$PREF{create_resized_copies_01__new_filename}		= '%%orig%%-small.%%ext%%';



# PREFs Section 15: Image Options.
############################################################################
# Some image files will be corrupt, or will be too big for a given server to
# resize within a reasonable amount of time.  These timeout settings let you
# tell FileChucker when to give up.  The settings are in seconds.
#
$PREF{image_thumbnail_creation_timeout}			= 8;
$PREF{video_thumbnail_creation_timeout}			= 8;
$PREF{automatic_image_resizing_timeout}			= 20;









# PREFs Section 16: Styling.
############################################################################
# Here you can adjust the CSS code to change the look and feel of
# FileChucker.  If you're embedding FileChucker in multiple different pages,
# and you want different styling on each one, you can create multiple copies
# of $PREF{css} here, named $PREF{css1}, $PREF{css2}, etc; then when you
# call FileChucker, pass ?css1, or ?css2, etc.
#
$PREF{css} = qq`

/* html { min-height: 100%; margin-bottom: 1px; } */   /* so #viewpath doesn't shift in FF when there's no scrollbar. -- update 200703: no longer needed since #viewpath is inside the table now. */

#fcbody { background: #ddd; color: #000; font-family: sans-serif; font-size: 0.8em; text-align: center; }
.popupstatusbody { background: #fff !important; }

#fcbody dl { margin: 0 0 1em; padding: 0; }
#fcbody dt, dd { margin: 0; padding: 0; }

#pb { margin: 14px auto 2px auto; padding: 3px; }
#pb a { color: #000; }
#pb a:hover { color: #aaa; }
#pb { position: absolute; left: -8000px; }
#fcfooter { color: #8b8f8b; margin: 24px auto 4px auto; font-size: 8pt; }

/* #uploaderpage, #filelistpage, #defaultpage etc, are the outer containers for their respective pages. */
#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage { width: 700px; margin: 15px auto; background: white; border: 1px solid #999; padding: 10px; }
#uploaderpage #title, #popupstatuspage #title, #uploadcompletepage #title, #filelistpage #title, #defaultpage #title { font-size: 200%; font-weight: bold; padding: 8px 0 15px 0; }
#uploaderpage, #uploadcompletepage { width: 450px; }
#uploaderpage #intro { text-align: center; margin: 0px auto 25px auto; }
#popupstatuspage { padding: 0; margin: 0 auto; }
#specialnote { font-weight: bold; }

#fc-container { /* padding: 8px 12px; */ } /* this is the whole page except for title and pb */
#fc-container a { color: #507090; }
#fc-container a:hover { color: #aaa; }

/* #progBarContainer includes everything (progress bar, text, table); #theMeter includes just the bar and the text (percent and rate) */
#progBarContainer { padding-top: 10px; }
#progBar, #progBarText	{ width: %PREF{progress_bar_width}px; }
#progBar { margin: 2px auto; height: 20px; border: 1px inset; background: #eee; text-align: left; }
#progBarDone { width: 0; height: 20px; border-right: 1px solid #444; background: #507090; background: #4a6695 url(%PREF{path_to_filelist_images}pb-bg-02.png) repeat-x; }
#theMeter { margin-bottom: 20px; }
#uploadCompleteMsg { width: %PREF{progress_bar_width}px; margin: 0 auto 20px; }
#progBarContainer table { width: %PREF{progress_bar_width}px; margin: 4px auto 20px auto; text-align: right; border-collapse: collapse; border: 0; border-bottom: 1px solid #bbb;}
#progBarContainer table td { border-top: 1px solid #bbb; text-align: center; }
#progBarContainer #upload-row-1, #progBarContainer #upload-row-3 { background: #e6e6e6; }
#progBarContainer #upload-row-2, #progBarContainer #upload-row-4 { background: #efefef; }

#progBarText	{ font-size: 90%; margin: 1px auto; white-space: nowrap; position: relative; }
#progRate	{ position: absolute; top: 0; left: 0; text-align: left; }
#progStatus	{ margin: 0 auto; text-align: center; font-style: italic; }
#progPercent	{ position: absolute; top: 0; right: 0; text-align: right; }

#theuploadform, #progBarPlaceholder, #uploadDoneContainer, #progBarContainer, #progBarContainer table { font-size: 9pt; } /* for sites that set their own ridiculous font sizes on general HTML elements instead of IDs and classes */

#fcuploadsummary { margin-top: 20px; margin-bottom: 20px !important; }
#fcuploadsummary dt { font-weight: bold; font-size: 120%; margin: 20px auto 10px auto; }
#fcuploadsummary dt.first { margin-top: 0; }
#fcuploadsummary dd { margin-bottom: 5px; }
#fcuploadsummary input { padding: 3px; }
#uploadstats dt { font-weight: bold; font-size: 120%; margin-bottom: 10px; }

td.headercell { font-weight: bold; }

%PREF{css_for_upload_progress_table}

#viewpath { white-space: nowrap; background: #efefef; margin: 0 auto 0 auto; padding: 0px 4px 0px 4px; }
#viewpath-outer { padding: 6px; }
#viewpath-inner { position: relative; height: 1.8em; }
#viewpath-text { text-align: left; position: absolute; left: 0; margin-top: 2px; }
#filelist #viewpath-text a { display: inline; }

div#optmenutop { text-align: right; position: absolute; right: 0; }
#optmenutop select, #optmenutop input			{ margin: 0; padding: 0; vertical-align: middle; font-size: 85%; }
.actionrow .controls select, .actionrow .controls input	{ margin: 0; padding: 0; vertical-align: middle; font-size: 85%; }
/* form#optionstop, form#optionsbottom { display: inline; margin: 0; padding: 0; } */

#optmenutop optgroup, #optmenubottom optgroup { font-weight: bold; font-style: normal; }
#optmenutop option, #optmenubottom option { padding-left: 20px; }

#filelist { text-align: left; border-collapse: collapse; margin: 2px auto; border: 1px solid #444; color: #000; width: 97%; }
#filelist tr { border: 0px solid white; }
#filelist tr.even { background: %PREF{filelist_row_normal_bgcolor_even}; }
#filelist tr.odd { background: %PREF{filelist_row_normal_bgcolor_odd}; }

/* Add these to replace the JS-based row mouseovers: 
#filelist tr.odd:hover, #filelist tr.even:hover { background: #507090; color: #fff; }
#filelist tr.odd:hover a, #filelist tr.even:hover a { color: #fff; }
*/

#filelist td { }
#filelist td#viewpath-cell { padding: 0; }
#filelist td#viewpath-cell a { text-decoration: underline; }
#filelistpage .pagelinks { margin-top: 20px; }

#filelist a:link { color: %PREF{filelist_row_normal_link_color}; text-decoration: none; display: block; width: 100%; padding: 4px 2px; }
#filelist a:visited { color: %PREF{filelist_row_visited_link_color}; text-decoration: none; display: block; width: 100%; padding: 4px 2px; }
#filelist a:hover { color: %PREF{filelist_row_hover_link_color}; }


#filelist .emptytable { text-align: center; font-style: italic; padding: 4px; }

#filelist td.pname { background: url(%PREF{path_to_filelist_images}fcarrow.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.fname { background: url(%PREF{path_to_filelist_images}fcfile.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.diricon { background: url(%PREF{path_to_filelist_images}fcfolder.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.homeicon { background: url(%PREF{path_to_filelist_images}fchome.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.dname { background-color: inherit; }
#filelist td.pname, #filelist td.dname, #filelist td.fname { width: 55%; padding-left: 20px; }
/* #filelist td.thumb { background-image: none; } */
#filelist img.fcthumb, #filelist img.fcvidthumb { border: 1px solid #000; }
#filelist .mimeicon, #filegrid .mimeicon { border: 0; }


#filelist .info, #filelist .mv, #filelist .sel, #filelist .del, #filelist .opt, #filelist .cinfo { text-align: center; }
#filelist .size { text-align: right; }
#filelist .size { white-space: pre; padding: 4px 10px 4px 2px; }
#filelist .date { white-space: pre; padding: 4px 5px; text-align: right; }
#filelist .info, #filelist .mv, #filelist .del, #filelist .sel, #filelist .opt, #filelist .cinfo { padding: 0 6px; }
#filelist .spc { padding: 0 6px 0 3px; }

#filelist .info, #filelist .cp, #filelist .mv, #filelist .sel, #filelist .mopts, #filelist .del, #filelist .perms { display: none; }
#filegrid .info, #filegrid .cp, #filegrid .mv, #filegrid .sel, #filegrid .mopts, #filegrid .del, #filegrid .perms { display: none; }
#filelist #infohead, #filelist #cphead, #filelist #mvhead, #filelist #selhead, #filelist #delhead, #filelist #moptshead, #filelist #permshead { display: none; }
#filegrid #infohead, #filegrid #cphead, #filegrid #mvhead, #filegrid #selhead, #filegrid #delhead, #filegrid #moptshead, #filegrid #permshead { display: none; }


.optsmenu { min-width: 90px; max-width: 150px; background: #eee; border: 1px solid #999; color: #000; text-align: left; }
.optsmenu a { display: block; text-decoration: none; padding: 5px; color: #000; }
.optsmenu div { display: block; padding: 5px; color: #555; white-space: nowrap; font-style: italic; }
.optsmenu a:hover { background: #c7c7c7; }

#filelist th { text-align: center; padding: 5px 0; font-size: 120%; background: #507090; color: #fff; border-bottom: 1px solid #444; }
#filelist #namehead { text-align: left; padding-left: 7px; }
#filelist #namehead a, #filelist #sizehead a, #filelist #datehead a { color: #fff; font-weight: bold; }


#filegrid { margin: 10px auto; text-align: center; }
#filegrid td { width: 33%; padding: 10px; border: 1px solid #fff; }
#filegrid td:hover { background: #efefef; border: 1px solid #bbb; }
#filegrid a.thumb { display: block; }
#filegrid a.icon { display: block; border: 0; }
#filegrid img.icon { border: 0; }
#filegrid .prnt .info, #filegrid .prnt .size, #filegrid .prnt .cp, #filegrid .prnt .mv, #filegrid .prnt .sel, #filegrid .prnt .del { display: none; }
#filegrid .dir .info, #filegrid .dir .sel { display: none; }
#filegrid td#viewpath-cell a { text-decoration: underline; }
#filegrid img.fcthumb, #filegrid img.fcvidthumb { border: 1px solid #000; }

#filegrid .pname a:link, #filegrid .dname a:link, #filegrid .fname a:link		{ color: #000; text-decoration: none; padding: 4px 2px; }
#filegrid .pname a:visited, #filegrid .dname a:visited, #filegrid .fname a:visited	{ color: #000; text-decoration: none; padding: 4px 2px; }
#filegrid .pname a:hover, #filegrid .dname a:hover, #filegrid .fname a:hover		{ color: #000; text-decoration: underline; }

#filegrid .date, #filegrid .size { font-size: 90%; color: #676767; }

#filegrid .emptytable { text-align: center; font-style: italic; padding: 4px; }


form#itemactions { margin: 0; padding: 0; }
#filelist .actionrow a:link, #filelist .actionrow a:visited, #filegrid .actionrow a:link, #filegrid .actionrow a:visited { text-decoration: none; display: inline; width: auto; padding: 0; margin: 0; }
td.actionrow { padding: 6px; text-align: right; vertical-align: middle; white-space: nowrap; }
#filegrid { width: 100%; }
.actionrow .sizeinfo	{ float: left; text-align: left; padding-left: 5px; margin-top: 2px; }
.actionrow .links	{ float: right; text-align: right; padding-right: 10px; margin-top: 2px; width: 20%; }
.actionrow .controls	{ float: right; text-align: right; padding-right: 5px; padding-left: 8px; }

.actionrow a.toggle-counts { text-decoration: underline !important; }

#fcinfo { border-collapse: collapse; border: 1px solid #ccc; background: #efefef; padding: 3px; }
#fcinfo tr:hover { background: #e0e0e0; }
#fcinfo td { border-top: 1px solid #ccc; padding: 4px;  }
#fcinfo .spacer { height: 25px; }
#fcinfo .f { text-align: left; width: 50%; font-weight: bold; }
#fcinfo .v { text-align: left; }
#fcinfo .h { text-align: left; font-size: 16pt; font-weight: bold; }



#setfilecount_wrapper { margin: 15px 0 12px 0; }
#fcbody form#theuploadform { margin: 15px auto; width: 96%; }
#filefields { }
#filefields .even { }
#filefields .odd { }
.fileelement { margin-bottom: 5px; }
.onesubgroup { padding: 10px 0; border-top: 1px solid #ddd; }
.onesubgroup div { margin-bottom: 5px; }
.onesubgroup label { display: inline; font-size: 100%; } /* we're centered by default, so we don't need the floats and clearfix-filefield stuff; just inline it. */
.onesubgroup label, .onesubgroup input, .onesubgroup select { margin: 2px 0; }
.onesubgroup picksubdir_label, .onesubgroup .newsubdir_label { }
.onesubgroup input.file { background: #eee; } /* compensate for weird width in Safari */
.upform_note { clear: both; }

#addanotherfile { margin-top: 15px; }

.fcfieldwrap
{
	border-top: 1px solid #ddd;
	padding: 8px;
}

#setfilecount_title { margin-bottom: 8px; }
#choosefiles_title { margin-top: 10px; }

#perfile-textboxes
{
	margin: 8px 20px;
}

#theuploadform textarea.upform_field
{
	height: 150px;
}
.radiobox
{
	margin-top: 3px !important;
	text-align: left;
}
#top-textboxes .radiobox,
#perfile-textboxes .radiobox,
#bottom-textboxes .radiobox
{
	float: left;
	width: 40%;
	display: block;
}

#uploadbutton { margin: 25px 0 10px 0; }
#uploadbuttonwrapper { border-top: 1px solid #ddd; }
.uploader-comments { text-align: left; border: 1px solid #e0e0e0; padding: 4px; }

.input_error { background-color: #FFDD00 !important; }




.onesubgroup label, .onesubgroup input, .onesubgroup select { margin: 7px 0; }

.upform_pair
{
	clear:both;
}
.upform_label
{
	float: left;
	width: 49%;
	text-align: left;
	padding: 3px 0;
}
#theuploadform .upform_field
{
	display: block;
	width: 49%;
	float: left;
}
#theuploadform input.text,
#theuploadform textarea.upform_field,
#theuploadform select.upform_field
{
	border: 1px solid #888;
	padding: 3px;
	background: #efefef;
}
#theuploadform input.text,
#theuploadform textarea.textarea
{
	width: 47%;
}
#theuploadform input.checkbox
{
	width: 15px;
}
#theuploadform .upform_field:hover, #theuploadform .upform_field:focus
{
	background: #fff;
}
.upform_note
{
	text-align: left;
	padding: 7px 0;
}




#fcbody .hr { height: 1px; border-bottom: 1px solid #000; margin: 15px 2px; line-height: 1px; }
#fcbody h1, #fcbody h2, #fcbody h3, #fcbody h4, #fcbody h5, #fcbody h6 { margin-top: 5px; margin-bottom: 5px; }
#fcbody form { margin: 0; padding: 0; }
#fcbody p { margin-top: 10px; margin-bottom: 10px; }

#selections_table
{
	border-collapse: collapse;
	border: 1px solid #9a9a9a;
	margin: 15px auto;
	text-align: left;
}
#selections_table .odd	{ background: #e6e6e6; }
#selections_table .even	{ background: #efefef; }
#selections_table td { padding: 4px 4px 4px 20px; background: url(%PREF{path_to_filelist_images}fcfile.gif) 1% 50% no-repeat; }

#place_order { text-align: center; }
#theorderform { width: 300px; margin: 0 auto; padding: 3px; text-align: left; border: 1px solid #999; background: #e6e6e6; }
#theorderform .text { width: 150px; margin: 5px; padding: 3px; border: 1px solid #676767; }
#theorderform .submit input { margin: 5px; }

#itemperms { border-collapse: collapse; border: 1px solid #bbb; text-align: center; margin: 10px auto; color: #575757; width: 90%; }
#itemperms th { background: #507090; color: #fff; padding: 12px; font: bold 16pt sans-serif; }
#itemperms .heading td { background: #83B96B; color: #fff; padding: 4px; font: bold 10pt sans-serif; }
#itemperms td { padding: 2px; }
#itemperms td.name { text-align: left; }
#itemperms td.path { text-align: left; }
#itemperms td.none { text-align: left; font-style: italic; }
#itemperms td.ro, #itemperms td.rw { text-align: left; padding-left: 80px; white-space: nowrap; }
#itemperms tr.odd { background: #e9e9e9; }
#itemperms tr.even { background: #efefef; }
#itemperms a { color: #000; }
#itemperms tr:hover { background: #83B96B; color: #fff; }
#itemperms tr:hover a { color: #fff; text-decoration: underline; }
#itemperms tr:hover a:hover { color: #000; }
.itemperms-letters { font-size: 120%; font-weight: bold; }
#fc-container .itemperms-letters a { padding: 4px; color: #507090; text-decoration: none; }
#fc-container .itemperms-letters a:hover { background: #507090; color: #fff; }
#fc-container .itemperms-letters a.current { text-decoration: underline; }
#itemperms .button { margin: 10px; }


.footnote { font: italic 9pt sans-serif; color: #888; margin: 5px 40px; }

.enc_tbl
{
	border: 1px solid #777;
	margin: 10px auto;
}
.enc_tbl table
{
	border-collapse: separate;
	border-spacing: 0;
	border: 0;
	background: #fff;
	width: 100%;
	margin: 0;
	font-size: 8pt;
}
.enc_tbl table th
{
	padding: 9px;
	background: #507090;
	color: #fff;
}
.enc_tbl td.verthead
{
	padding: 9px;
	background: #507090;
	color: #fff;
	width: 50%;
}
.enc_tbl table th a, .enc_tbl td.verthead a
{
	color: #fff !important;
	text-decoration: none;
}
.enc_tbl table td a, .enc_tbl table td a:visited
{
	color: #000 !important;
	border: 0;
}
.enc_tbl table td
{
	padding: 7px;
	border-bottom: 1px solid #fff;
}
.enc_tbl table td.vertcell
{
	border-bottom: 1px solid #fff;
}
.enc_tbl table tr
{
	border-bottom: 1px solid #fff;
}
.enc_tbl table tr.odd
{
	padding: 4px;
	background: #f4f6f8;
	background: #f1f1f1;
	background: #efefef;
}
.enc_tbl table tr.even
{
	padding: 4px;
	background: #ffffff;
	background: #fafafa;
	background: #e9e9e9;
}
.enc_tbl table tr:hover
{
	background: #fcffb8;
	background: #d5d9d3;
}
.pagelinks span, .pagelinks a
{
	margin: 4px;
}
.enc_tbl input.text
{
	width: 200px !important;
	border: 1px solid #555;
	padding: 3px;
}
.enc_tbl textarea
{
	border: 1px solid #555;
	padding: 3px;
}
.enc_tbl textarea.shorttext
{
	width: 300px;
	height: 50px;
}
.enc_tbl textarea.mediumtext
{
	width: 300px;
	height: 80px;
}
.enc_tbl textarea.longtext
{
	width: 300px;
	height: 200px;
}
.enc_tbl .readonly
{
	margin-left: 5px;
}
#database_deleter
{
	margin: 30px 0;
	padding: 0;
}
.enc_create_tbl table
{
	/* width: auto; */
}
.enc_create_tbl th, .enc_create_tbl td,
.enc_edit_tbl th, .enc_edit_tbl td
{
	text-align: left;
}
.enc_create_tbl td.button, .enc_edit_tbl td.button
{
	text-align: center;
}


.encmenu { border: 1px solid #777; margin: 5px auto 20px auto; max-width: 400px; text-align: center; }
.encmenu a { display: block; padding: 5px; border: 0; color: #000 !important; border-top: 1px solid #fff; text-decoration: none; }
.encmenu a.odd { background: #efefef; }
.encmenu a.even { background: #e9e9e9; }
.encmenu a:visited { border: 0; border-top: 1px solid #fff; }
.encmenu a.first, .encmenu a.first:visited { border: 0; }
.encmenu a:hover { background: #d5d9d3; text-decoration: none; }
.encmenu .header { background: #507090; color: #fff; font: bold 8pt sans-serif; padding: 12px; }


.altcolor1 { color: #ffd200; }


.clear { height: 0; line-height: 0; font-size: 0; clear: both; }

.clearfixtb:after {
    content: "."; 
    display: block; 
    height: 0; 
    clear: both; 
    visibility: hidden;
}

.clearfixtb { display: inline-block; }

/* Hides from IE-mac \*/
* html .clearfixtb {height: 1%;}
.clearfixtb {display: block;}
/* End hide from IE-mac */



.clearfix:after {
    content: "."; 
    display: block; 
    height: 0; 
    clear: both; 
    visibility: hidden;
}

.clearfix { display: inline-block; }

/* Hides from IE-mac \*/
* html .clearfix {height: 1%;}
.clearfix {display: block;}
/* End hide from IE-mac */

`;



$PREF{css_for_upload_progress_table___hook} = qq`
#tca1,#tcb1,#tcc1,#tcd1 { width: 25%; }
#tca2,#donef,#leftf,#totalf { width: 25%; }
#tca3,#dones,#lefts,#totals { width: 25%; }
#tca4,#donet,#leftt,#totalt { width: 25%; }
`;



$PREF{css_for_upload_progress_table___nonhook} = qq`
#tca1,#tcb1,#tcc1,#tcd1 { width: 33%; }
#tca2,#donef,#leftf,#totalf { position: absolute; left: -10000px; overflow: hidden; height: 0; }
#tca3,#dones,#lefts,#totals { width: 34%; }
#tca4,#donet,#leftt,#totalt { width: 33%; }
`;



$PREF{css_light} = qq`
#filelist tr.actionrow { background: #507090; color: #fff; }
#filelist td.actionrow { border-top: 1px solid #444; }
#filelist .actionrow a:link { color: #fff; }
#filelist .actionrow a:visited { color: #fff; }
#filelist .actionrow a:hover, #filelist .actionrow a:visited:hover { color: #000; }
#filelist td#viewpath-cell a { color: #507090; }
#filelist td#viewpath-cell a:hover { color: #aaa; }

#filegrid td#viewpath-cell { background: #efefef; border: 1px solid #bbb; padding: 2px; }
#filegrid td.actionrow { background: #efefef; border: 1px solid #bbb; }
`;

$PREF{css_light_ie} = qq``;



$PREF{css_big} = qq`
/* big blocky style: */
#filelist a:link, #filelist a:visited {  }
#filelist th, #filelist td { padding: 10px 6px; }
#filelist th { font-size: 140%; }
#filelist td.pname { background: url(%PREF{path_to_filelist_images}fcarrowbig.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.dname { background: url(%PREF{path_to_filelist_images}fcfolderbig.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.fname { background: url(%PREF{path_to_filelist_images}fcfilebig.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.pname, #filelist td.dname, #filelist td.fname { width: 350px; padding-left: 15px; }
#filelist td.pname a:link, #filelist td.dname a:link, #filelist td.fname a:link, td.pname, #filelist td.pname a:visited { color: black; font-size: 14px; font-weight: bold; text-decoration: none; }
#filelist td.dname a:visited, #filelist td.fname a:visited { color: #000; font-size: 14px; font-weight: bold; text-decoration: none; }
#filelist td.pname a:hover, #filelist td.dname a:hover, #filelist td.fname a:hover {  }
#filelist td.dname { padding-top: 12px; padding-bottom: 8px; }
#filelist tr.actionrow { background: #507090; color: #fff; }
#filelist td.actionrow { border-top: 1px solid #444; }
#filelist .actionrow a:link { color: #fff; }
#filelist .actionrow a:visited { color: #fff; }
#filelist .actionrow a:hover, #filelist .actionrow a:visited:hover { color: #000; }

#filelist td#viewpath-cell a { color: #507090; }
#filelist td#viewpath-cell a:hover { color: #aaa; }
#filelist td#viewpath-cell { background: #efefef; padding: 2px; }

#filegrid td#viewpath-cell { background: #efefef; border: 1px solid #bbb; padding: 2px; }
#filegrid td.actionrow { background: #efefef; border: 1px solid #bbb; }
`;

$PREF{css_big_ie} = qq``;



$PREF{css_dark} = qq`
#fcbody { background: #434343; color: #fff; }
#title { padding-top: 10px !important; color: #fff; }
#intro { margin: 0 7px; }
#fc-container a { color: #ccc; }
#fc-container a:hover { color: #000; }
#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage { background: #5a775a; border: 0px; padding: 0; padding-bottom: 10px; }
#fc-container { padding: 0; margin: 0; }
#uploaderpage { width: 600px; padding-top: 12px; }
#uploadbuttonwrapper { margin: 15px 5px; }
#progBarContainer table { color: #fff; background: #424242; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#progBarContainer #upload-row-1, #progBarContainer #upload-row-3 { background: #545454; }
#progBarContainer #upload-row-2, #progBarContainer #upload-row-4 { background: #545454; }
#progBarContainer table td#tca1,#progBarContainer table td#tca2,#progBarContainer table td#tca3,#progBarContainer table td#tca4 { border-top: 0; }
#dones,#lefts,#totals,#donef,#leftf,#totalf,#donet,#leftt,#totalt { border-top: 1px solid #676767; }
#progBar { background: #6a6a6a; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#progBarDone { border-right: 1px solid #000; background: #993333; }
#filefields { background: #333; background: transparent; color: #000; margin: 0px 20px; border: 1px solid #393939; }
#filefields .even { background: #5a6d5a; }
#filefields div { margin-top: 8px; margin-bottom: 12px; }
.onesubgroup { padding: 3px 0; }
#top-textboxes, #perfile-textboxes, #bottom-textboxes { margin: 25px 20px; padding: 5px; border: 1px solid #393939; }
table#filelist { color: %PREF{filelist_row_normal_text_color}; border: 1px solid #333; border-bottom: 1px solid #333;  margin: 0 auto 20px auto; }
#filelist th { background: #333; border-bottom: 0px solid #000; }
#filelist td { border-top: 1px solid #676767; }
#filelist a:hover { color: #fff; }
#filelist td#viewpath-cell { border-top: 0; border-bottom: 1px solid #676767; padding: 0; }
#filelist td#viewpath-cell a:hover { color: #000; }

#viewpath { background: %PREF{filelist_row_normal_bgcolor_even}; }

#filegrid { width: 95%; }
#filegrid { border-collapse: collapse; }
#filegrid td { border: 0; }
#filegrid td:hover { border: 0; background: #648564; }
#filegrid .date, #filegrid .size { font-size: 90%; color: #fff; }
#filegrid td.actionrow { background: %PREF{filelist_row_normal_bgcolor_even}; border: 1px solid #333; }
#filegrid td#viewpath-cell { background: %PREF{filelist_row_normal_bgcolor_even}; border: 1px solid #333; padding: 3px; }

#filelist tr.actionrow { background: #333; }
#filelist td.actionrow { border-top: 1px solid #444; }
#filelist .actionrow a:link { color: #fff; }
#filelist .actionrow a:visited { color: #fff; }
#filelist .actionrow a:hover, #filelist .actionrow a:visited:hover { color: #000; }
#filelist td.actionrow { background: #333; border: 1px solid #333; }

#fcfooter { background: #333; margin-top: 0; padding: 10px 4px; }
#fcfooter a { color: #fff; text-decoration: none; font-weight: bold; }
#fcfooter a:hover { color: #aa3333; }
`;

$PREF{css_dark_ie} = qq``;



$PREF{css_darker} = qq`
#fcbody { background: #434343; color: #fff; }
#title { color: #fff; }
#fc-container a { color: #aaa; }
#fc-container a:hover { color: #fff; }
#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage { background: #575757; border: 0; border-top: 1px solid #fff; border-left: 1px solid #fff; border-bottom: 1px solid #000; border-right: 1px solid #000; }
#progBarContainer table { color: #fff; background: #424242; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#progBarContainer #upload-row-1, #progBarContainer #upload-row-3 { background: #424242; }
#progBarContainer #upload-row-2, #progBarContainer #upload-row-4 { background: #4a4a4a; }
#progBarContainer table td { border: 0; }
#progBar { background: #424242; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#progBarDone { border-right: 1px solid #444; background: #4a774a; }
#filefields { border: 0px solid #393939; background: #4a774a; color: black; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#filefields div { margin-top: 8px; margin-bottom: 12px; }
table#filelist { border: 0px solid #000; color: %PREF{filelist_row_normal_text_color}; border-top: 1px solid #000; border-left: 1px solid #000; border-bottom: 1px solid #fff; border-right: 1px solid #fff; }
#filelist th { background: #437743; border-bottom: 0px solid #000; }
/* input,select { background: #000; color: #fff; border: 2px inset #fff; } */
`;

$PREF{css_darker_ie} = qq``;



$PREF{css_minimal} = qq`
/* minimal style: */
#fcbody { background: #fff; font-family: serif; }
#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage { border: 0; }
#filelistpage #title { position: absolute; left: -10000px; }
#fcfooter { color: #555; }
#fcfooter a { color: #000; }
#fcfooter a:hover { color: #507090; }
#pb a { color: #737373; }
#pb a:hover { color: #000; }
#uploader { background: #fff; border: 0; }
#filelist { border: 1px dashed #bbb; border-left: 0; border-right: 0; }
#filelist tr { border-top: 1px dashed #bbb; }
#filelist tr.even { background: %PREF{filelist_row_normal_bgcolor_even}; background: #fff; }
#filelist tr.odd { background: %PREF{filelist_row_normal_bgcolor_odd}; background: #fff; }
#filelist a:link, #filelist a:visited {  }
#filelist th, #filelist td { padding: 1px 6px; font-size: 0.8em; }
#filelist th { font-size: 0.9em; color: #000; background: #fff; border-bottom: 0; }
#filelist #namehead a, #filelist #sizehead a, #filelist #datehead a { color: #000; }
#filelist td.pname { background: url(%PREF{path_to_filelist_images}fcarrow.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.dname { background: url(%PREF{path_to_filelist_images}fcfolder.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.fname { background: url(%PREF{path_to_filelist_images}fcfile.gif) 1% 50% no-repeat; background-color: inherit; }
#filelist td.pname, #filelist td.dname, #filelist td.fname { width: 350px; padding-left: 18px; }
#filelist td.pname a:link, #filelist td.dname a:link, #filelist td.fname a:link, td.pname, #filelist td.pname a:visited { color: black; text-decoration: none; }
#filelist td.dname a:visited, #filelist td.fname a:visited { color: #555; text-decoration: none; }
#filelist td.pname a:hover, #filelist td.dname a:hover, #filelist td.fname a:hover { }
td.size { color: #444; }
td.date { color: #444; }
`;

$PREF{css_minimal_ie} = qq``;



$PREF{css_round} = qq`
/* round style: */
#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage { padding: 0; border: 0; }
#fcbody { background: #e3e3e3; }
#fcc1 { background: url(%PREF{path_to_filelist_images}fcc-TL-e3e3e3.png) top left no-repeat; }
#fcc2 { background: url(%PREF{path_to_filelist_images}fcc-TR-e3e3e3.png) top right no-repeat; }
#fcc3 { background: url(%PREF{path_to_filelist_images}fcc-BR-e3e3e3.png) bottom right no-repeat; }
#fcc4 { background: url(%PREF{path_to_filelist_images}fcc-BL-e3e3e3.png) bottom left no-repeat; }

#title img { margin: 10px auto 0px auto; }
#uploaderpage #title, #uploadcompletepage #title, #filelistpage #title, #defaultpage #title { padding: 10px 1px 1px 1px; color: #53a4cd; }
#fc-container, #intro { margin-top: 0px; padding-top: 0px; }
#uploaderpage #fcfooter { margin-bottom: 15px; font-size: 8pt; }

table#filelist { border: 0px solid #ccc; color: #444; width: 630px; margin: 10px auto 0 auto; }
#filelist th { background: #e3e3e3; border: 0; font-size: 90%; padding: 0px; color: #878787; }
#filelist #namehead a, #filelist #sizehead a, #filelist #datehead a { color: #878787; font-weight: bold; }
#filelist td { border-top: 1px solid #ddd; font-size: 8.5pt; }
#filelist td.actionrow { background: #e3e3e3; border-bottom: 1px solid #ddd; }
#filelist td.actionrow a:hover { color: #888; }
#filelist td#viewpath-cell { border-top: 0; border-bottom: 1px solid #ddd; background: transparent; padding: 0; }
#filelist td#viewpath-cell a:hover { color: #53a4cd; text-decoration: underline; }

#filegrid { margin: 10px auto 0 auto; border-collapse: collapse; background: #efefef; width: 630px; }
#filegrid td { border: 0; }
#filegrid td:hover { border: 0; background: #e6e6e6; }
#filegrid td.actionrow { background: #e3e3e3; border-top: 1px solid #bbb; border-bottom: 1px solid #bbb; }
#filegrid td.actionrow .links a { font-size: 8pt; }

#filegrid td#viewpath-cell { border-top: 0; border-bottom: 1px solid #bbb; background: transparent; padding: 0; }
#viewpath { background: #efefef url(%PREF{path_to_filelist_images}fcc-TL-efefef.png) top left no-repeat; color: #53a4cd; margin: 0px auto 0px auto; text-align: left; border: 0; padding: 0; font-size: 8.5pt; }
#viewpath-outer { padding: 0; }
#viewpath-inner { background: url(%PREF{path_to_filelist_images}fcc-TR-efefef.png) top right no-repeat; height: 3.8em; }
#viewpath-text { padding: 10px 5px 10px 15px; font-size: 110%; font-weight: bold; font-family: Tahoma, Arial, sans-serif; letter-spacing: 1px; }
#optmenutop { padding: 12px 15px 10px 5px; font-size: 10pt; }

#filelistpage #fcfooter { background: #efefef url(%PREF{path_to_filelist_images}fcc-BR-efefef.png) bottom right no-repeat; color: #444; margin: 0px auto 10px auto; width: 630px; font-size: 8pt; }
#filelistpage #fcfooter-inner { background: url(%PREF{path_to_filelist_images}fcc-BL-efefef.png) bottom left no-repeat; width: 630px; }
#filelistpage #fcfooter-text { padding: 14px; }

#fc-container a { font-weight: bold; }
#fc-container #fcfooter a { color: #65c460; text-decoration: none; font-size: 10pt; }
#fc-container #fcfooter a:hover { background: #65c460; color: white; }
`;

$PREF{css_round_ie} = qq``;



$PREF{css_shadowdark} = qq`

#filelist tr.actionrow { background: #507090; color: #fff; }
#filelist td.actionrow { border-top: 1px solid #444; }
#filelist .actionrow a:link { color: #fff; }
#filelist .actionrow a:visited { color: #fff; }
#filelist .actionrow a:hover, #filelist .actionrow a:visited:hover { color: #000; }
#filelist td#viewpath-cell a { color: #507090; }
#filelist td#viewpath-cell a:hover { color: #aaa; }

#filegrid td#viewpath-cell { background: #efefef; border: 1px solid #bbb; padding: 2px; }
#filegrid td.actionrow { background: #efefef; border: 1px solid #bbb; }


#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage
{
	border: 0;
	margin: 0 auto;
}

#fcbody { background: #abaab0; }

/* default styling, for most pages: */
#fcwrapper  { width: 750px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-center-750px.png) repeat-y; }
#fcwraphead { width: 750px; height: 15px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-top-750px.png) no-repeat; }
#fcwrapfoot { width: 750px; height: 15px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-bottom-750px.png) no-repeat; }

/* narrower styling for uploader and uploadcomplete pages: */
.uploaderbody #fcwrapper,  .uploadcompletebody #fcwrapper  { width: 500px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-center-500px.png) repeat-y; }
.uploaderbody #fcwraphead, .uploadcompletebody #fcwraphead { width: 500px; height: 15px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-top-500px.png) no-repeat; }
.uploaderbody #fcwrapfoot, .uploadcompletebody #fcwrapfoot { width: 500px; height: 15px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-30-bottom-500px.png) no-repeat; }

/* narrower/bare styling for popupstatus page: */
.popupstatusbody #fcwrapper, .popupstatusbody #fcwraphead, .popupstatusbody #fcwrapfoot
{
	width: auto; background-image: none; height: auto;
}

`;

$PREF{css_shadowdark_ie} = qq``;



$PREF{css_shadowlight} = qq`

#filelist tr.actionrow { background: #507090; color: #fff; }
#filelist td.actionrow { border-top: 1px solid #444; }
#filelist .actionrow a:link { color: #fff; }
#filelist .actionrow a:visited { color: #fff; }
#filelist .actionrow a:hover, #filelist .actionrow a:visited:hover { color: #000; }
#filelist td#viewpath-cell a { color: #507090; }
#filelist td#viewpath-cell a:hover { color: #aaa; }

#filegrid td#viewpath-cell { background: #efefef; border: 1px solid #bbb; padding: 2px; }
#filegrid td.actionrow { background: #efefef; border: 1px solid #bbb; }


#uploaderpage, #uploadcompletepage, #filelistpage, #defaultpage
{
	border: 0;
	margin: 0 auto;
}

#fcbody { background: #eee; }

/* default styling, for most pages: */
#fcwrapper  { width: 750px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-20-center-750px.png) repeat-y; }
#fcwraphead { width: 750px; height: 15px; margin: 0 auto; background: transparent url(%PREF{path_to_filelist_images}shadowbg-20-top-750px.png) no-repeat; }
#fcwrapfoot { width: 750px; height: 15px; margin: 0 auto; background: transparent url(%PREF{path_to_filelist_images}shadowbg-20-bottom-750px.png) no-repeat; }

/* narrower styling for uploader and uploadcomplete pages: */
.uploaderbody #fcwrapper,  .uploadcompletebody #fcwrapper  { width: 500px; margin: 0 auto; background: url(%PREF{path_to_filelist_images}shadowbg-20-center-500px.png) repeat-y; }
.uploaderbody #fcwraphead, .uploadcompletebody #fcwraphead { width: 500px; height: 15px; margin: 0 auto; background: transparent url(%PREF{path_to_filelist_images}shadowbg-20-top-500px.png) no-repeat; }
.uploaderbody #fcwrapfoot, .uploadcompletebody #fcwrapfoot { width: 500px; height: 15px; margin: 0 auto; background: transparent url(%PREF{path_to_filelist_images}shadowbg-20-bottom-500px.png) no-repeat; }

/* narrower/bare styling for popupstatus page: */
.popupstatusbody #fcwrapper, .popupstatusbody #fcwraphead, .popupstatusbody #fcwrapfoot
{
	width: auto; background-image: none; height: auto;
}

`;

$PREF{css_shadowlight_ie6} = qq`
#fcbody { background: #fff; }
`;













# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# By default, if your server's version of the CGI.pm module is >= 3.03,
# then we'll use its upload hook.  If it's older than 3.03, we'll do it
# manually, since older versions don't support the upload hook.  This 
# means we can't show the counts for number of files completed/remaining,
# but if your server has an ancient version of the CGI.pm module, then
# you have no choice.  Anyway, this PREF is in case the script isn't
# working for you, even though you DO have v3.03 or newer.  Setting this
# to 'yes' will force the manual behavior, and the only loss will be the
# aforementioned files-completed/files-remaining; the time and size will
# still display properly.
#
# When not using the upload hook functionality (either because you disable
# it here, or because FileChucker automatically disables it because your
# server's version of Perl doesn't support it) you can specify an amount
# of time to sleep during each pass of the while() loop that uploads the
# data from the client.  Decrease this value to make uploads faster; or
# increase it to cut down on the server load.
#
$PREF{disable_upload_hook}				= 'no';
$PREF{sleep_time_during_nonhook_uploads}		= 0.03; # in seconds.



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# On servers that are slow or overloaded, increasing the delay between
# progress bar updates may help.  The default value is 700 (in milliseconds)
# so you might want to increase this to, say, 2000 or 4000.
#
$PREF{progressbar_update_delay}				= 700;



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# FileChucker can use a database backend instead of diskfiles to store
# its temporary working data, if you'd like.  There's really no benefit
# of one method over the other (and on servers that perform write-caching,
# thus preventing the progress bar from working properly, the database 
# backend doesn't actually work around the problem, as we had thought it
# might).
#
# For this to work, your database username (in PREFs Section 12) needs 
# privileges for INSERT, UPDATE, SELECT, DELETE, and CREATE.  If you're
# paranoid and don't want to give it CREATE privs, then see the
# create_db_table_for_temp_data() function to find out the column types,
# so you can create the table manually.
#
# THIS FEATURE IS CURRENTLY INCOMPLETE.
#
#$PREF{use_database_for_temp_data}			= 'no';
#$PREF{table_name_for_temp_data}			= 'temp_upload_data';



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# You probably don't want the temp-data entries filling up your DB since
# they don't actually contain any useful information after the upload is
# complete.  But you can disable this if for some reason you want them kept.
# Note that this doesn't delete the uploaded files; they aren't stored in
# the database.
#
$PREF{purge_temp_data_immediately}			= 'yes';



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# If you're using FileChucker in a way where it doesn't make sense for the
# default page to be the uploader, you can change that here.  Currently the
# options are 'uploader' and 'filelist'.
#
$PREF{default_page}					= 'uploader';



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# If you want to use Ko instead of KB, etc, you can set those labels here.
# Note that you should not change these to Kb or Mb, since lowercase-b means
# "bit", not "byte", so all the displayed values would be incorrect.
#
$PREF{KB}						= 'KB';
$PREF{MB}						= 'MB';



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# Specify the length of the serial number and whether it should be all
# numbers or can also contain letters.  A length less than 10 is NOT a
# good idea because the smaller the value, the better the chance that
# there will be collisions between simultaneous uploads.  But even 10
# is pretty low; 20 is better, and 30 is the default.
#
# You can also choose to use a hash for the serial, in which case the
# length and use_letters options have no effect.
#
$PREF{length_of_serial}					= 30;
$PREF{use_letters_in_serial}				= 'yes';
$PREF{use_hash_for_serial}				= 'yes';
$PREF{cut_serial_to_this_length_even_after_hashing}	= 0; # zero to disable.



# PREFs Section Z:  Misc Settings Not Usually Needed.
############################################################################
# FileChucker will always look for a file named filechucker_prefs.cgi to read
# preference settings from.  But you can also create other prefs files in case
# you want to run FileChucker with different settings depending on how it's 
# called.  There are 2 methods for this:
#
# The first and recommended method is the shortcut method.  This requires you to
# specify (within filechucker.cgi or filechucker_prefs.cgi) shortcut names and
# shortcut targets.  Then you pass the shortcut_name on the URL with ?prefs=foo
# and that will cause FileChucker to use the filename specified in shortcut_target
# for shortcut_name = foo.  For example, given these settings:
#
#	$PREF{other_prefs_files}{01}{shortcut_name}	= qq`foo`;
#	$PREF{other_prefs_files}{01}{shortcut_target}	= qq`bar_prefs.txt`;
#
# ...then this URL:
#
#	http://example.com/cgi-bin/filechucker.cgi?prefs=foo
#
# ...will cause FileChucker to load prefs from the bar_prefs.txt file.
#
# The second method allows you to specify the full prefs filename including
# path on the URL with ?prefsfile=/cgi-bin/foo/bar/baz.txt.  The advantage of
# this method is that you don't have to specify the allowable prefs files 
# beforehand; the disadvantage is that, although we do our best to untaint
# filenames coming from the URL, accepting filenames to execute from the URL
# which any user can specify is always something of a security risk.  So
# using the shortcut method instead is more secure because FileChucker will
# only use filenames that you have hard-coded into either filechucker.cgi or
# filechucker_prefs.cgi beforehand.
#
# For either method, the _in_docroot PREF controls whether we'll automatically
# prepend your $DOCROOT value onto the filenames that you specify.  On most
# servers, if you put your prefs files in the same folder as filechucker.cgi,
# and you specify the filenames here with no path information, then the script
# will find them OK with _in_docroot set to 'no'.  Using in_docroot = 'no' also
# allows you to specify the full path with the filenames, all the way from the
# root of your server.  Using _in_docroot = 'yes' allows you to specify the
# filenames with just the website portion of the path, for example you could
# say {shortcut_target} = qq`/cgi-bin/client_prefs.txt`.
#
$PREF{other_prefs_files}{01}{shortcut_name}		= 'clients';
$PREF{other_prefs_files}{01}{shortcut_target}		= 'clients_prefs.txt';
$PREF{other_prefs_files}{02}{shortcut_name}		= 'vendors';
$PREF{other_prefs_files}{02}{shortcut_target}		= 'vendors_prefs.txt';
#
$PREF{enable_other_prefs_files_with_filename_on_URL}	= 'no';
$PREF{other_prefs_filenames_from_URL_can_contain_paths}	= 'no';
#
$PREF{other_prefs_files_are_in_docroot}			= 'no';


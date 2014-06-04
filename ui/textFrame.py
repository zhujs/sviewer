

from gi.repository import Gtk, Gdk

class textFrame( Gtk.Frame ):
	"""Implement the a frame showing the message we required"""
	def __init__(self, label=None ):
		super( textFrame, self).__init__()
		self.set_label_align( 0.0, 1.0 )
		self.set_shadow_type( Gtk.ShadowType.ETCHED_OUT )
		
		# set the markup of label in the frame
		header = Gtk.Label()
		header.set_markup( label )
		self.set_label_widget( header )
		self.set_opacity( 1 ) 

	def addText( self, text ):
		"""Show the text Message in the textView"""
		textView = Gtk.TextView()
		textBuffer = textView.get_buffer()
		textBuffer.set_text( text )
		
		# the text is not editable 	
		textView.set_editable( False )
		textView.set_cursor_visible( False )
		textView.set_wrap_mode( Gtk.WrapMode.WORD )
		
		textView.set_border_width( 10 )
		self.add( textView )
		
		
                



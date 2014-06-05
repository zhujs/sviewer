
from gi.repository import Gtk,Gdk
from ui import window 


class Viewer( object ):
	def __init__( self ):
		self.display = Gdk.Display.get_default()
		self.primaryClipboard = Gtk.Clipboard.get_for_display( self.display, Gdk.SELECTION_PRIMARY )
		
		# resgister the owner-change signal for the primary clipboard
		self.primaryClipboard.connect( "owner-change", self._onClipboardChange )
		self.win = window.PopupWin()
	
	def _onClipboardChange( self , clipboard, event ):
		
		try:
			text = clipboard.wait_for_text( )
			
			if text is not None and text.strip() != "":
				self.win.hide()
				# get the pointer position
				x, y = self._get_pointer_position()

				self.win.show_all()	
				self.win.set_keep_above( True )
				self.win.move( x+10, y+10 )


		except Exception as e:
			print e	

	def _get_pointer_position(self):
		"""get the current position of the pointer, (0,0) is upper left corner"""
		try:
			deviceManager = self.display.get_device_manager()
			pointer = deviceManager.get_client_pointer()

			# get the pointer device position
			screen, x, y = pointer.get_position()
		except Exception as e:
			print e
			x, y = (0,0)
		finally:
			return x, y

	def run( self ):
		Gtk.main()

if __name__ == "__main__":
	Viewer().run()





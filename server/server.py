# Server 
print("Starting Server")

class db():
    """
    Database
    """
    username = ['Alex','sero']
    message = ['Hello', 'hi']

    
class score():
    def get_message(parameter_list):
        """
        Get Message
        """        
        print(db.username[0],db.message[0])
        

    def send_message(parameter_list):
        """
        Send Message
        """
        pass

score.get_message(parameter_list=1)
from flask import Blueprint, render_template, request
from flask_login import login_required
from app import app, regular_employee_rol_need
from ZK import ZK, const
import sys
import os
import json
from datetime import datetime

control_clock = Blueprint("control_clocks", __name__)

@control_clock.before_request
@login_required
@regular_employee_rol_need
def constructor():
   pass

@control_clock.route("/control_clocks", methods=['GET'])
def index():
   zk = ZK('10.98.15.1', 
            port=4370, 
            timeout=5, 
            password='0', 
            force_udp=False, 
            ommit_ping=False)
   try:
      conn = zk.connect()
      attendance = conn.get_attendance()
      conn.disconnect()
      data = []
      for atten in attendance:
         data.append({'user_id': atten.user_id,'timestamp':str(atten.timestamp),'status':atten.status,'punch':atten.punch})
      return {'status':'success','attendance' : data}
   except Exception as e:
      return {'status' : format(e)}

@control_clock.route("/control_clocks/users", methods=['GET'])
def users():
   conn = None
   # create ZK instance
   zk = ZK('192.168.1.249', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
   try:
      # connect to device
      conn = zk.connect()
      # disable device, this method ensures no activity on the device while the process is run
      conn.disable_device()
      # another commands will be here!
      # Example: Get All Users
      users = conn.get_users()
      user_data = []
      i = 0
      for user in users:
         privilege = 'User'
         if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
            print ('+ UID #{}'.format(user.uid))
            print ('  Name       : {}'.format(user.name))
            print ('  Privilege  : {}'.format(privilege))
            print ('  Password   : {}'.format(user.password))
            print ('  Group ID   : {}'.format(user.group_id))
            print ('  User  ID   : {}'.format(user.user_id))

            user_data[i] = user.name
   
            i = i + 1

      return str(1)
   except Exception as e:
      return ("Process terminate : {}".format(e))
   finally:
      if conn:
         conn.disconnect()

@control_clock.route("/control_clocks/create", methods=['GET'])
def create(self=''):
   zk = ZK('192.168.1.201', 
            port=4370, 
            timeout=5, 
            password='0', 
            force_udp=False, 
            ommit_ping=False)
   try:
      conn = zk.connect()
      set_user = conn.set_user(uid=1000, name='Jesus Cova', privilege=const.USER_DEFAULT, password='12345678', group_id='', user_id='27141', card=0)
      conn.disconnect()
      
      return {'status':'success','set_user' : set_user}
   except Exception as e:
      return {'status' : format(e)}

@control_clock.route("/control_clocks/delete", methods=['GET'])
def delete():
   zk = ZK('192.168.1.201', 
            port=4370, 
            timeout=5, 
            password='0', 
            force_udp=False, 
            ommit_ping=False)
   try:
      conn = zk.connect()
      zk.delete_user(user_id=271413998)
      conn.disconnect()
      
      return {'status':'success'}
   except Exception as e:
      return {'status' : format(e)}


@control_clock.route("/control_clocks/zk", methods=['GET'])
def zk():
   zk = ZK('192.168.1.249', 
            port=4370, 
            timeout=5, 
            password='0', 
            force_udp=False, 
            ommit_ping=False)
   try:
      conn = zk.connect()
      zktime = conn.get_time()
      print(zktime)
      
      return {'status':'success'}
   except Exception as e:
      return {'status' : format(e)}


@control_clock.route("/control_clocks/watch", methods=['GET'])
def watch():
   zk = ZK('192.168.1.201', 
               port=4370, 
               timeout=5, 
               password='0', 
               force_udp=False, 
               ommit_ping=False)
      
   try:
      conn = zk.connect()
      zktime = conn.get_time()
      print(zktime)
      # update new time to machine
      newtime = datetime.today()
      print(newtime)
      conn.set_time(newtime)
      
      return {'status':'success'}
   except Exception as e:
      return {'status' : format(e)}


@control_clock.route("/control_clocks/store", methods=['POST'])
def store():
   print(1)
   return str(2)

LOGIN_SCHEMA = {"type": "object",
                "properties":
                    {
                        "user": {"type": "object",
                                 "properties":
                                     {
                                         "id": {"type": "number"},
                                         "email": {"type": "string"},
                                         "name": {"type": "string"},
                                         "phone": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                         "city": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                         "aboutSelf": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                         "avatar": {"type": "string", "optional": True},
                                         "sex": {"anyOf": [{"type": "string"}, {"type": "null"}]},
                                         "userChangePassword": {"type": "boolean"},
                                         "role": {"type": "string"},
                                     }
                                 },
                        "schools": {"type": "array",
                                    "items":
                                        {"type": "object",
                                         "properties":
                                             {
                                                 "id": {"type": "number"},
                                                 "description": {"type": "string"},
                                                 "name": {"type": "string"},
                                                 "slug": {"type": "string"},
                                                 "domain": {"type": "string"},
                                                 "avatar": {"type": "string"},
                                                 "logo": {"type": "string"},
                                                 "logocover": {"type": "string"},
                                                 "primaryColor": {"type": "string"},
                                                 "favicon": {"type": "string"},
                                                 "role": {"type": "string"},
                                             }
                                         }
                                    }
                    }
                }
